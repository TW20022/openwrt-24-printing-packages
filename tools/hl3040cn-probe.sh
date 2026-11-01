#!/bin/sh
# ============================================================
# Brother HL-3040CN 打印数据完整性探针 v1（无需真实打印机）
#
#   hl3040cn-selftest.sh 只回答"链路通不通"，本脚本回答"数据整不整"：
#   同一份文档连打 N 次，逐份统计 PJL 结构，判断是整页输出还是被截断。
#
#   判读依据（从 brhl3040cnfilter.bin 的字符串表确认）：
#     \033%-12345X                 UEL，通用语言退出
#     @PJL JOB NAME="..."          作业开始
#     @PJL ENTER LANGUAGE=XL2HB    每页一次
#     ) BROTHER XL2HB;             每页数据块开始
#     @PJL EOJ NAME="..."          作业收尾 —— 被截断时不会有
#   完整输出的结构是：
#     UEL + JOB + ... + ENTER LANGUAGE + )BROTHER + <二进制> + UEL + EOJ + UEL
#
#   用法： sh hl3040cn-probe.sh [次数，默认 3]
# ============================================================
PPD=/usr/share/ppd/hl3040cn.ppd
[ -f "$PPD" ] || PPD=/usr/share/cups/model/brother/hl3040cn.ppd
Q=HL_PROBE
B=/usr/lib/cups/backend/savefile
TXT=/tmp/probe.txt
N=${1:-3}
OUTDIR=/tmp/probe

ok()   { printf '  [ OK ] %s\n' "$1"; }
bad()  { printf '  [FAIL] %s\n' "$1"; }
warn() { printf '  [ ?? ] %s\n' "$1"; }
info() { printf '  ---- %s\n' "$1"; }
hr()   { printf '\n===== %s =====\n' "$1"; }

# 统计某个字面量在二进制文件里出现的次数
cnt() { grep -a -o -- "$2" "$1" 2>/dev/null | wc -l | tr -d ' '; }

# 尾部 120 字节可读化
tailview() { tail -c 120 "$1" | tr -c '[:print:]\n' '.'; }

# 分析一份落盘文件
analyse() {
  f=$1
  sz=$(wc -c < "$f")
  uel=$(cnt "$f" '%-12345X')
  lang=$(cnt "$f" '@PJL ENTER LANGUAGE=XL2HB')
  blk=$(cnt "$f" ') BROTHER XL2HB;')
  eoj=$(cnt "$f" '@PJL EOJ')

  printf '  %-28s %8s 字节  UEL=%s  页(ENTER)=%s  块=%s  EOJ=%s\n' \
         "$(basename "$f")" "$sz" "$uel" "$lang" "$blk" "$eoj"

  # 完整性判定：有 EOJ 才说明 filter 走完了收尾流程
  if [ "$eoj" -ge 1 ] && [ "$lang" -ge 1 ]; then
    if tail -c 200 "$f" | grep -aq '%-12345X'; then
      ok "结构完整（含 EOJ 且以 UEL 结束）"
    else
      warn "有 EOJ 但尾部没有 UEL，收尾可能不完整"
    fi
  elif [ "$lang" -ge 1 ]; then
    bad "有 XL2HB 数据段但没有 @PJL EOJ —— 数据在收尾前被掐断"
  else
    bad "没有 XL2HB 数据段"
  fi
  info "尾部: $(tailview "$f")"
}

hr "0. 准备"
[ -x "$B" ] || {
  cat > $B <<'EOS'
#!/bin/sh
[ -z "$1" ] && exit 0
[ "$1" = "-" ] && exit 0
cat > "/tmp/savefile-$1-$2.prn"
echo "INFO: saved"
exit 0
EOS
  chmod 755 $B
}
ok "假 backend: $B"
printf 'probe page\nline 2 1234567890\n' > $TXT
info "测试文档: $TXT ($(wc -c < $TXT) 字节)，连打 $N 次"
rm -rf $OUTDIR; mkdir -p $OUTDIR

/etc/init.d/cupsd start >/dev/null 2>&1
sleep 2
lpstat -r >/dev/null 2>&1 || { bad "cupsd 起不来"; exit 1; }

lpadmin -x $Q >/dev/null 2>&1
made=0
for i in 1 2 3; do
  lpadmin -p $Q -v savefile:/tmp/dummy -P "$PPD" -E 2>/dev/null && { made=1; break; }
  sleep 3
done
[ $made -eq 1 ] && ok "队列 $Q 就绪" || { bad "lpadmin 失败"; exit 1; }

job_wait() {   # job_wait <作业号>
  jw=0
  while [ $jw -lt 120 ]; do
    lpstat -W not-completed -o 2>/dev/null | awk '{print $1}' | grep -qx "$1" || return 0
    sleep 2; jw=$((jw+2))
  done
  return 1
}

hr "1. 连打 $N 次，逐份分析"
i=1
while [ $i -le $N ]; do
  rm -f /tmp/savefile-*.prn
  jid=$(lp -d $Q $TXT 2>&1 | sed -n 's/.*request id is \([^ ]*\).*/\1/p')
  if [ -z "$jid" ]; then bad "第 $i 次提交失败"; break; fi
  job_wait "$jid" || warn "第 $i 次作业 120 秒未结束"
  sleep 1
  got=0
  for f in /tmp/savefile-*.prn; do
    [ -f "$f" ] || continue
    cp "$f" "$OUTDIR/run$i-$(basename "$f")"
    got=1
  done
  if [ $got -eq 1 ]; then
    for f in $OUTDIR/run$i-*; do analyse "$f"; done
  else
    bad "第 $i 次没有落盘文件"
  fi
  i=$((i+1))
done

hr "2. 一致性对比"
szs=$(for f in $OUTDIR/run*; do wc -c < "$f"; done | sort -n | uniq | tr '\n' ' ')
info "各次字节数（去重）: $szs"
nuniq=$(for f in $OUTDIR/run*; do wc -c < "$f"; done | sort -u | wc -l)
if [ "$nuniq" -eq 1 ]; then
  ok "多次结果完全一致 —— 输出确定性，无竞态"
else
  warn "多次结果大小不一致（$nuniq 种）—— 存在时序差异，需看 EOJ 是否都齐全"
fi

hr "3. 收尾"
lpadmin -x $Q >/dev/null 2>&1 && ok "已删除队列 $Q"
info "样本保留在 $OUTDIR/ 供进一步分析"
info "如需手工复查某一页： grep -a -o '%-12345X' <文件> | wc -l"
