#!/bin/sh
# hplip-fw-deploy.sh —— 给 hplip 补齐 ZJS 机型固件 + 持久化插件状态（OpenWrt）
#
# 背景
#   HP LaserJet 1000/1005/1018/1020、P1005~P1009/P1505/P1102/P1102w/P1566 属"软固件"机型：
#   板子没有非易失存储，固件每次上电都要由主机灌进 RAM，断电即失效。
#   hplip 的自动链本来是完整的：
#       hotplug.d/usb/10-hp-printer → hp-config_usb_printer → hp-firmware
#           → base/device.py: downloadFirmware() 读 data/firmware/<model>.fw.gz → libusb 直写
#   但 13 个 .fw.gz 是 HP 专有许可，只随 hplip-plugin 分发，不在开源 hplip 里；
#   本 feed 的 hplip 包（install 只装 data/{ldl,models,pcl,ps}）也没有它们
#   → 自动链每次死在 "Firmware file '...' not found"。
#   本脚本补上这些文件，并修掉 /var 是 tmpfs 导致插件状态丢失的问题。
#
# 为什么用软链而不是改路径
#   installer/pluginhandler.py 里 PLUGIN_STATE_FILE = '/var/lib/hp/hplip.state' 是硬编码；
#   但也不能改成 /etc/hplip.state —— base/g.py 的 ConfigBase.write() 有白名单：
#       if filename.startswith("/root/") or filename.startswith("/etc/"):
#           log.error("attempted to write to '%s'" % self.filename); return
#   写 /etc 会被静默丢弃。软链之所以成立，是因为写入时传入的仍是 /var/lib/hp/hplip.state
#   （能过白名单），open(...,"w") 穿透软链写到 /etc 目标；用的是截断写不是 rename，
#   软链本身不会被打断。=> 软链 + tmpfs 重建后补链，是当前代码下唯一安全的做法。
#
# 用法
#   sh hplip-fw-deploy.sh                          # 只体检，不写文件
#   sh hplip-fw-deploy.sh --deploy --src /tmp/fw   # 部署 13 个 .fw.gz（目录或 tar.gz）
#   sh hplip-fw-deploy.sh --persist                # 插件状态持久化
#   sh hplip-fw-deploy.sh --now                    # 部署 + 状态 + 立刻给在插的机器灌一次
#   sh hplip-fw-deploy.sh --remove                 # 撤掉本脚本装的东西
#   --src <目录|tar.gz>   固件源；省略时依次找 ./firmware、/tmp/firmware、/root/firmware
#   --model <段名>        强制机型，如 hp_laserjet_1020（PID 撞号时用）
#   --force               跳过 FWVER 去重与冲突告警
#
# 它不做什么
#   不装"自己写 /dev/usb/lp*"的 hotplug 规则 —— 那是 foo2zjs 的通道
#   （tools/foo2zjs-fw-setup.sh）。两条通道同时灌固件会让设备挂死。
#   本脚本只补料，下发仍由 hplip 的 10-hp-printer 负责。

set -u
FWDIR=/usr/share/hplip/data/firmware
MODELS=/usr/share/hplip/data/models/models.dat
STATE_ETC=/etc/hplip.state
STATE_VAR=/var/lib/hp/hplip.state
STATE_HOOK=/etc/hotplug.d/usb/05-hplip-state
LOCKDIR=/var/lock/hplip-fw.lock

# 文件名必须与 models.dat 段名小写严格一致，改一个字 hp-firmware 就找不到。
# 注意 p1102w：hplip 3.25.6 的 models.dat 里没有这个段（只有 hp_laserjet_professional_p1102，
# 且它的 fw-download=False），所以这个文件是"孤儿"—— 部署了也不会被查找，留着无害。
FILES="hp_laserjet_1000 hp_laserjet_1005_series hp_laserjet_1018 hp_laserjet_1020
hp_laserjet_p1005 hp_laserjet_p1006 hp_laserjet_p1007 hp_laserjet_p1008 hp_laserjet_p1009
hp_laserjet_p1505 hp_laserjet_professional_p1102 hp_laserjet_professional_p1102w
hp_laserjet_professional_p1566"
ORPHAN="hp_laserjet_professional_p1102w"

MODE=check
SRC=""
MODEL=""
FORCE=0

ok()   { echo "  [ OK ] $*"; }
bad()  { echo "  [FAIL] $*"; }
warn() { echo "  [WARN] $*"; }
info() { echo "  ---- $*"; }
hr()   { echo; echo "===== $* ====="; }

usage() {
    sed -n '/^# 用法/,/^# 它不做什么/p' "$0" | sed 's/^# \{0,1\}//'
}

while [ $# -gt 0 ]; do
    case "$1" in
        --check)   MODE=check ;;
        --deploy)  MODE=deploy ;;
        --persist) MODE=persist ;;
        --now)     MODE=now ;;
        --remove)  MODE=remove ;;
        --force)   FORCE=1 ;;
        --src)     shift; SRC="${1:-}" ;;
        --model)   shift; MODEL="${1:-}" ;;
        -h|--help) usage; exit 0 ;;
        *)         echo "未知参数：$1（--help 看用法）"; exit 2 ;;
    esac
    shift
done

[ "$(id -u)" = "0" ] || { echo "需要 root 运行"; exit 1; }
PWDIR=$(dirname "$0")

# ---------------------------------------------------------------- 0 环境
hr "0. 环境"
info "内核 $(uname -r)"

[ -x /usr/bin/hp-firmware ] && ok "hp-firmware 在位" || bad "没有 /usr/bin/hp-firmware —— 先装 hplip-tools"

if [ -s "$MODELS" ]; then
    ok "models.dat 在位（$(grep -c '^\[' "$MODELS" 2>/dev/null) 个机型）"
else
    bad "缺 $MODELS —— hplip 基础包没装好"
fi

[ -d /usr/share/hplip/data ] && ok "/usr/share/hplip/data 存在" || bad "缺 /usr/share/hplip/data"

if [ -d /sys/module/usblp ]; then
    ok "usblp 已加载（可用 usb_printerid 做 FWVER 预检）"
else
    warn "usblp 未加载 —— 不影响 hplip 灌固件（走 libusb），但没法预检 FWVER"
fi

for c in md5sum tar sed grep; do
    command -v $c >/dev/null 2>&1 || warn "$c 未安装"
done

if [ -L "$STATE_VAR" ]; then
    ok "插件状态已是软链：$STATE_VAR -> $(readlink "$STATE_VAR")"
elif [ -s "$STATE_VAR" ]; then
    warn "插件状态在 tmpfs 里（$STATE_VAR），重启即丢 —— 跑 --persist 修掉"
elif [ -s "$STATE_ETC" ]; then
    info "只有 $STATE_ETC（tmpfs 里还没链上）—— 跑 --persist 补链"
else
    info "未见插件状态（插件可能没装过；不影响固件下发，只影响 hplip 打印侧）"
fi

# ---------------------------------------------------------------- 1 冲突
hr "1. 与其它固件下发通道的冲突"
CONFLICT=0
for f in /etc/hotplug.d/usb/*; do
    [ -f "$f" ] || continue
    case "$f" in */10-hp-printer|*/05-hplip-state) continue ;; esac
    if grep -qs 'usb/lp\|sihp\|foo2zjs\|firmware' "$f"; then
        CONFLICT=1
        warn "另一条固件下发规则：$f"
        info "它多半是 foo2zjs 路线（cat *.dl > /dev/usb/lp*），与 hplip 的 libusb 通道互斥"
        info "同一次插拔两边都灌 → 固件流交错 → 设备挂死。二选一："
        info "  走 hplip  ：删掉 $f（或 sh $PWDIR/foo2zjs-fw-setup.sh --remove）"
        info "  走 foo2zjs：别用本脚本，改用 foo2zjs-fw-setup.sh --install"
    fi
done
[ "$CONFLICT" = "0" ] && ok "没有第三方固件下发规则，通道独占"

if [ -x /etc/hotplug.d/usb/10-hp-printer ]; then
    ok "10-hp-printer 可执行（自动下发由它负责，本脚本不重复实现）"
else
    warn "10-hp-printer 不存在或不可执行 —— 部署了固件也不会自动下发"
fi

# ---------------------------------------------------------------- 2 固件源
hr "2. 固件源"
SRCDIR=""
TMPDIR_FW=""

if [ -n "$SRC" ]; then
    if [ -d "$SRC" ]; then
        SRCDIR=$SRC
    elif [ -f "$SRC" ]; then
        TMPDIR_FW=/tmp/.hplip-fw-$$
        mkdir -p "$TMPDIR_FW"
        if tar -xzf "$SRC" -C "$TMPDIR_FW" 2>/dev/null; then
            for d in "$TMPDIR_FW" "$TMPDIR_FW"/*; do
                [ -d "$d" ] || continue
                if ls "$d"/*.fw.gz >/dev/null 2>&1; then SRCDIR=$d; break; fi
            done
            [ -n "$SRCDIR" ] || SRCDIR=$TMPDIR_FW
        else
            bad "解包失败：$SRC"
        fi
    else
        bad "固件源不存在：$SRC"
    fi
else
    for d in "$PWDIR/firmware" /tmp/firmware /root/firmware; do
        if [ -d "$d" ] && ls "$d"/*.fw.gz >/dev/null 2>&1; then SRCDIR=$d; break; fi
    done
fi

if [ -n "$SRCDIR" ]; then
    ok "固件源：$SRCDIR（$(ls "$SRCDIR"/*.fw.gz 2>/dev/null | wc -l | tr -d ' ') 个 .fw.gz）"
else
    warn "未找到固件源（用 --src 指向插件里的 firmware/ 目录或 tar 包）"
fi

# ---------------------------------------------------------------- 3 部署
hr "3. 部署到 $FWDIR"
if [ "$MODE" = "check" ]; then
    info "体检模式，不写文件"
elif [ "$MODE" = "remove" ]; then
    info "remove 模式跳过部署"
elif [ -z "$SRCDIR" ]; then
    bad "无固件源，无法部署"
elif [ "$SRCDIR" = "$FWDIR" ]; then
    info "源与目标同目录，只做校验"
else
    mkdir -p "$FWDIR"
    n_new=0; n_same=0; n_miss=0
    for k in $FILES; do
        s=$SRCDIR/$k.fw.gz
        t=$FWDIR/$k.fw.gz
        if [ ! -s "$s" ]; then
            n_miss=$((n_miss+1)); warn "源里缺 $k.fw.gz"; continue
        fi
        if [ -s "$t" ] && [ "$(md5sum "$s" | cut -d' ' -f1)" = "$(md5sum "$t" | cut -d' ' -f1)" ]; then
            n_same=$((n_same+1)); continue
        fi
        [ -s "$t" ] && warn "$k.fw.gz 已存在但内容不同 → 覆盖"
        cp "$s" "$t" 2>/dev/null && n_new=$((n_new+1)) || bad "拷贝失败：$k"
    done
    chmod 644 "$FWDIR"/*.fw.gz 2>/dev/null
    ok "新增/更新 $n_new 个，已一致 $n_same 个，源里缺 $n_miss 个"
fi

# ---------------------------------------------------------------- 4 对齐校验
hr "4. 文件名 / models.dat 对齐"
if [ -d "$FWDIR" ] && [ -s "$MODELS" ]; then
    n_ok=0; n_skip=0
    for f in "$FWDIR"/*.fw.gz; do
        [ -f "$f" ] || continue
        k=$(basename "$f" .fw.gz)
        if grep -q "^\[$k\]" "$MODELS"; then
            n_ok=$((n_ok+1))
        else
            n_skip=$((n_skip+1))
            warn "$k.fw.gz 在 models.dat 里没有同名段 —— hplip 不会查找它"
            [ "$k" = "$ORPHAN" ] && info "  （已知孤儿：P1102w 在 3.25.6 里无段，p1102 的 fw-download 本身是 False，留着无害）"
        fi
    done
    ok "可用 $n_ok 个，孤儿 $n_skip 个"
    info "体积参考：1000=50236 1005_series=52233 1018=70543 1020=70412"
    info "          p1005/1007=153404 p1006/1008/1009=153487 p1505=166020"
else
    warn "跳过（缺 $FWDIR 或 $MODELS）"
fi

# ---------------------------------------------------------------- 5 状态持久化
hr "5. 插件状态持久化"
do_persist() {
    if [ -L "$STATE_VAR" ]; then
        ok "软链已在"
    elif [ -s "$STATE_VAR" ]; then
        if [ ! -s "$STATE_ETC" ]; then
            cp "$STATE_VAR" "$STATE_ETC" && chmod 644 "$STATE_ETC" && ok "当前状态已落到 $STATE_ETC"
        else
            info "$STATE_ETC 已存在，不覆盖（tmpfs 里的现存版本仍有效）"
        fi
    elif [ -s "$STATE_ETC" ]; then
        info "只有 $STATE_ETC，下面补链"
    else
        warn "两处都没有状态文件 —— 插件没装成功过"
        info "不伪造 installed=1：假的 installed 会让 hpcups 去加载并不存在的 lj.so"
        info "顺序应是：hp-plugin -i -p /tmp/hplip-3.25.6-plugin.run → 再跑本脚本 --persist"
        return 1
    fi

    mkdir -p /var/lib/hp
    ln -sf "$STATE_ETC" "$STATE_VAR" && ok "$STATE_VAR -> $STATE_ETC"

    mkdir -p "${STATE_HOOK%/*}"
    cat > "$STATE_HOOK" <<'EOS'
#!/bin/sh
# 由 hplip-fw-deploy.sh 安装：tmpfs 重建后把插件状态软链补回去。
# 05 开头是为了排在 10-hp-printer 之前（run-parts 按名排序）。
[ -e /var/lib/hp/hplip.state ] && exit 0
[ -s /etc/hplip.state ] || exit 0
mkdir -p /var/lib/hp
ln -sf /etc/hplip.state /var/lib/hp/hplip.state
EOS
    chmod 755 "$STATE_HOOK"
    ok "已装 $STATE_HOOK（USB 事件先自愈补链，赶在 10-hp-printer 之前）"

    jver=$(sed -n "s/^__version__ *= *'\([0-9.]*\)'.*/\1/p" /usr/share/hplip/base/version.py 2>/dev/null | head -1)
    [ -n "$jver" ] || jver=$(sed -n 's/^__version__ *= *"\([0-9.]*\)".*/\1/p' /usr/share/hplip/base/version.py 2>/dev/null | head -1)
    sver=$(sed -n 's/^version *= *//p' "$STATE_ETC" 2>/dev/null | head -1)
    if [ -n "$jver" ] && [ -n "$sver" ]; then
        if [ "$jver" = "$sver" ]; then
            ok "状态版本 $sver 与 hplip 一致"
        else
            warn "状态版本 $sver ≠ hplip $jver → 判 version mismatch（等同未安装）"
            sed -i "s/^version *=.*/version = $jver/" "$STATE_ETC" && ok "已改成 $jver"
        fi
    fi
}

case "$MODE" in
    check) info "体检模式，不改状态（要修就跑 --persist）" ;;
    remove)
        rm -f "$STATE_HOOK" && ok "已删 $STATE_HOOK"
        info "保留 $STATE_ETC 与 $FWDIR（插件状态和固件不属于临时产物）"
        ;;
    *) do_persist || true ;;
esac

# ---------------------------------------------------------------- 6 立即下发
hr "6. 立即下发（仅 --now）"

lp_to_id() {
    for d in "/sys/class/usb/${1##*/}/device" "/sys/class/usb/${1##*/}/device/.." \
             "/sys/class/usb/${1##*/}/device/../.."; do
        [ -r "$d/busnum" ] || continue
        printf '%03d:%03d' "$(cat "$d/busnum" 2>/dev/null)" "$(cat "$d/devnum" 2>/dev/null)"
        return 0
    done
    return 1
}

usb_list() {
    for d in /sys/bus/usb/devices/*/; do
        [ -r "$d/idVendor" ] || continue
        [ "$(cat "$d/idVendor" 2>/dev/null)" = "03f0" ] || continue
        b=$(cat "$d/busnum" 2>/dev/null); n=$(cat "$d/devnum" 2>/dev/null)
        [ -n "$b" ] && [ -n "$n" ] || continue
        printf '%03d:%03d %s:%s\n' "$b" "$n" "03f0" "$(cat "$d/idProduct" 2>/dev/null)"
    done
}

# 冷启动 PID → 固件 key（来源 foo2zjs hplj1000 的硬编码表）
fw_for_pid() {
    case "$1" in
        0517) echo hp_laserjet_1000 ;;
        1317) echo hp_laserjet_1005_series ;;
        4117) echo "" ;;
        2b17) echo hp_laserjet_1020 ;;
        3d17) echo hp_laserjet_p1005 ;;
        3e17) echo hp_laserjet_p1006 ;;
        4817) echo hp_laserjet_p1007 ;;
        4917) echo hp_laserjet_p1008 ;;
        3f17) echo hp_laserjet_p1505 ;;
        092a) echo hp_laserjet_professional_p1566 ;;
        002a) echo hp_laserjet_professional_p1102 ;;
        *)    echo "" ;;
    esac
}

# IEEE-1284 的 MDL → 固件 key（长名优先，避免 P1005 被 *1005* 抢走）
fw_for_mdl() {
    case "$1" in
        *P1005*|*p1005*) echo hp_laserjet_p1005 ;;
        *P1006*|*p1006*) echo hp_laserjet_p1006 ;;
        *P1007*|*p1007*) echo hp_laserjet_p1007 ;;
        *P1008*|*p1008*) echo hp_laserjet_p1008 ;;
        *P1009*|*p1009*) echo hp_laserjet_p1009 ;;
        *P1505*|*p1505*) echo hp_laserjet_p1505 ;;
        *P1102*|*p1102*) echo hp_laserjet_professional_p1102 ;;
        *P1566*|*p1566*) echo hp_laserjet_professional_p1566 ;;
        *1020*)          echo hp_laserjet_1020 ;;
        *1018*)          echo hp_laserjet_1018 ;;
        *1005*)          echo hp_laserjet_1005_series ;;
        *1000*)          echo hp_laserjet_1000 ;;
        *)               echo "" ;;
    esac
}

if [ "$MODE" != "now" ]; then
    info "跳过（要立刻灌一次：--now）"
elif ! command -v hp-firmware >/dev/null 2>&1; then
    bad "没有 hp-firmware，无法下发"
else
    DEVS=$(usb_list)
    if [ -z "$DEVS" ]; then
        warn "没看到 03f0:* 设备（没插 / 已断电）"
        info "固件已就位，下次插电由 10-hp-printer 自动下发"
    else
        info "现场 HP 设备：$(echo "$DEVS" | awk '{printf "%s ", $2}')"
        SEL=""

        # 1) 有 usblp 时按 IEEE-1284 的 MDL 判型（4117 共号时唯一可靠）
        for lp in /dev/usb/lp*; do
            [ -c "$lp" ] || continue
            id=$(usb_printerid "$lp" 2>/dev/null)
            case "$id" in *FWVER:*) warn "$lp 已有固件（FWVER），跳过"; continue ;; esac
            mdl=$(echo "$id" | sed -n 's/.*MDL:\([^;]*\).*/\1/p')
            [ -n "$mdl" ] || continue
            k=$(fw_for_mdl "$mdl")
            [ -n "$k" ] || continue
            [ -n "$MODEL" ] && [ "$MODEL" != "$k" ] && continue
            SEL=$(lp_to_id "$lp")
            MODEL=$k
            ok "识别到 $mdl → $k（$SEL）"
            break
        done

        # 2) 退路：用冷启动 PID 表
        if [ -z "$SEL" ] && [ -z "$MODEL" ]; then
            bid=$(echo "$DEVS" | head -1 | awk '{print $1}')
            pid=$(echo "$DEVS" | head -1 | awk '{print $2}' | cut -d: -f2)
            k=$(fw_for_pid "$pid")
            if [ -n "$k" ]; then
                MODEL=$k; SEL=$bid
                info "按冷启动 PID $pid 判型 → $MODEL"
            else
                warn "PID $pid 无法判型（4117 是 1018/P1005~P1008/P1505 灌后共号）"
                info "用 --model 指定：--now --model hp_laserjet_1020"
            fi
        fi

        # 3) 指定了 model 但还没定位设备：取第一台 HP
        [ -n "$MODEL" ] && [ -z "$SEL" ] && SEL=$(echo "$DEVS" | head -1 | awk '{print $1}')

        # 4) FWVER 去重（hplip 自己不做，重复灌会打断正在打印的作业）
        if [ -n "$SEL" ] && [ "$FORCE" != "1" ]; then
            for lp in /dev/usb/lp*; do
                [ -c "$lp" ] || continue
                [ "$(lp_to_id "$lp")" = "$SEL" ] || continue
                if usb_printerid "$lp" 2>/dev/null | grep -q FWVER; then
                    ok "该设备已带固件（$lp 有 FWVER），不重复灌；确需重灌加 --force"
                    SEL=""
                fi
                break
            done
        fi

        if [ -z "$SEL" ]; then
            info "本次不下发，等下次插拔由 10-hp-printer 处理"
        elif [ ! -s "$FWDIR/$MODEL.fw.gz" ]; then
            bad "$FWDIR/$MODEL.fw.gz 不存在，无法下发"
        else
            # hpmud 不能并发写，busybox 没有 flock → mkdir 原子锁
            if mkdir "$LOCKDIR" 2>/dev/null; then
                trap 'rmdir "$LOCKDIR" 2>/dev/null' EXIT INT TERM
                info "下发 $MODEL.fw.gz → $SEL"
                hp-firmware -y3 -s "$SEL" 2>&1 | tail -6 | sed 's/^/      /'
                sleep 2
                for lp in /dev/usb/lp*; do
                    [ -c "$lp" ] || continue
                    v=$(usb_printerid "$lp" 2>/dev/null | sed -n 's/.*\(FWVER:[^;]*\).*/\1/p')
                    [ -n "$v" ] && ok "$lp 已读出 $v"
                done
                rmdir "$LOCKDIR" 2>/dev/null
                trap - EXIT INT TERM
            else
                warn "另一个下发进程正在跑（$LOCKDIR 存在），本次跳过"
            fi
        fi
    fi
fi

# ---------------------------------------------------------------- 7 收尾
hr "7. 之后怎么走"
cat <<'EOS'
  · 部署完不用重启：10-hp-printer 在下次 bind 时自己会找到 .fw.gz。
  · 验证三连：
      ls -l /usr/share/hplip/data/firmware/*.fw.gz     # 13 个，644
      logread -f | grep -E 'hp-hotplug|hp1020fw'       # 插拔时看有没有下发记录
      usb_printerid /dev/usb/lp0 | grep FWVER          # 有 FWVER 即灌进去了
  · P 系列灌完固件 PID 会从 3d17/3e17/3f17 变成 4117，会再触发一次 bind；
    hplip 无 FWVER 去重，正在打印时被重灌会掉作业 —— 这就是脚本要预检 FWVER 的原因。
    （P1006 的 3e17 与 P1009 撞号，但两者固件字节完全相同：md5 cc655ae3...，灌哪个都一样。）
  · hplip 能打印这些机型的前提是插件的 lj.so 有对应架构：
    arm32/arm64/x86_32/x86_64 有，mips 没有 → MT7621 请用 foo2zjs 打印（固件仍可用本脚本下发）。
EOS

[ -n "$TMPDIR_FW" ] && rm -rf "$TMPDIR_FW"
exit 0
