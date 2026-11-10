#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 printer-models.md 生成「打印机型号速查」移动端单文件页面。

用法：python3 build-printer-lookup.py
输入：同目录 printer-models.md
输出：output/printer-lookup/index.html 与根目录 printer-models-mobile.html
页面完全自包含（数据内嵌、无外部请求），可直接保存到手机离线打开。
"""
import argparse
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "printer-models.md"
OUT_DIR = ROOT / "output" / "printer-lookup"
OUT_PAGE = OUT_DIR / "index.html"
OUT_SINGLE = ROOT / "printer-models-mobile.html"

PKGS = ["gutenprint", "hplip", "foo2zjs", "splix", "brlaser", "brhl3040cn"]
FAM_KEYS = [
    ("PCL", "PCL 系列"),
    ("Epson", "Epson ESC/P2 喷墨"),
    ("Canon", "Canon 喷墨"),
    ("热升华", "热升华 / 热转印"),
    ("DPL", "DPL 标签打印"),
    ("Lexmark", "Lexmark 喷墨"),
    ("PostScript", "通用 PostScript"),
    ("RAW", "RAW 直通"),
]
FAMS = [name for _, name in FAM_KEYS]

# 每个驱动包的标签配色：浅色 bg / 浅色 fg / 深色 bg / 深色 fg
TAG_COLORS = [
    ("#e8f0fe", "#1d4ed8", "rgba(59,130,246,.18)", "#93c5fd"),
    ("#f1eafe", "#6d28d9", "rgba(167,139,250,.18)", "#c4b5fd"),
    ("#d9f5f0", "#0f766e", "rgba(45,212,191,.16)", "#5eead4"),
    ("#fff0e0", "#b45309", "rgba(251,146,60,.18)", "#fdba74"),
    ("#e6f4e1", "#15803d", "rgba(74,222,128,.16)", "#86efac"),
    ("#eceef2", "#475569", "rgba(148,163,184,.18)", "#cbd5e1"),
]

HEADER_SKIP = {
    "型号", "驱动包", "驱动", "统计口径", "内容", "驱动名", "覆盖品牌",
    "物理机型（去重后）", "原始条目", "被 gutenprint 覆盖",
}


def parse_markdown(text):
    rows = []
    pkg = None
    fam = -1
    seen_families = []

    for line in text.splitlines():
        if line.startswith("## "):
            title = line[3:].strip().lower()
            pkg = next((p for p in PKGS if title.startswith(p)), None)
            fam = -1
            continue
        if line.startswith("### "):
            title = line[4:].strip()
            fam = -1
            if pkg == "gutenprint":
                for key, name in FAM_KEYS:
                    if key.lower() in title.lower():
                        fam = FAMS.index(name)
                        if name not in seen_families:
                            seen_families.append(name)
                        break
            continue
        if pkg is None or not line.startswith("|"):
            continue

        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or cells[0] in HEADER_SKIP:
            continue
        if all(set(c) <= set("-: ") for c in cells):
            continue
        model = cells[0].strip("* ").strip()
        if not model or model.startswith("**"):
            continue

        info = cells[1].strip() if len(cells) > 1 else ""
        note = cells[2].strip() if len(cells) > 2 else ""
        if pkg == "gutenprint":
            info = info.strip("`").strip()
            note = "" if note == "备注" else note
        elif pkg == "brlaser":
            info = ""
        exp = 1 if "EXPERIMENTAL" in (info + note).upper() else 0
        rows.append([PKGS.index(pkg), fam, model, info, note, exp])

    return rows, seen_families


def extract_stats(text):
    unique = re.search(r"\*\*跨栈去重后\*\*\s*\|\s*—\s*\|\s*\*\*([\d]+)\*\*", text)
    exclusive = re.search(r"\*\*([\d]+)\s*款[\s\S]*?为\s*hplip\s*独占\*\*", text)
    return {
        "unique": int(unique.group(1)) if unique else None,
        "exclusive": int(exclusive.group(1)) if exclusive else None,
    }


TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#f4f6f9" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#12151a" media="(prefers-color-scheme: dark)">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="format-detection" content="telephone=no">
<title>打印机型号速查 · OpenWrt 打印驱动</title>
<style>
:root{
  --bg:#f4f6f9; --surface:#ffffff; --surface2:#f8fafc; --text:#171a1f;
  --muted:#66707d; --line:#e3e7ed; --accent:#2563eb; --accent-soft:#e8f0fe;
  --warn:#b45309; --warn-bg:#fef3c7; --shadow:0 1px 2px rgba(16,24,40,.05);
}
@media (prefers-color-scheme: dark){
  :root{
    --bg:#12151a; --surface:#1b2028; --surface2:#222831; --text:#e8eaed;
    --muted:#98a2b3; --line:#2c343f; --accent:#60a5fa; --accent-soft:rgba(96,165,250,.14);
    --warn:#fbbf24; --warn-bg:rgba(251,191,36,.12); --shadow:none;
  }
}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
[hidden]{display:none!important}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--text);
  font:16px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif}
button,input{font:inherit;color:inherit}
button{cursor:pointer;border:0;background:none}
.wrap{max-width:760px;margin:0 auto;padding:0 12px calc(96px + env(safe-area-inset-bottom))}
header{position:sticky;top:0;z-index:20;background:var(--surface);border-bottom:1px solid var(--line);
  padding:10px 12px 8px;box-shadow:var(--shadow)}
.hd{max-width:760px;margin:0 auto}
.hd-row{display:flex;align-items:baseline;gap:8px;margin-bottom:8px}
.hd h1{font-size:17px;margin:0;font-weight:650;letter-spacing:.2px}
.hd .sub{font-size:12px;color:var(--muted);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.searchbox{position:relative;display:flex;align-items:center}
.searchbox svg{position:absolute;left:11px;width:18px;height:18px;fill:var(--muted);pointer-events:none}
#q{width:100%;min-height:44px;padding:10px 76px 10px 36px;border:1px solid var(--line);
  border-radius:12px;background:var(--surface2);outline:none;font-size:16px;
  -webkit-appearance:none;appearance:none}
#q:focus{border-color:var(--accent);box-shadow:0 0 0 3px var(--accent-soft)}
#clear{position:absolute;right:6px;width:36px;height:36px;border-radius:9px;color:var(--muted);
  display:none;align-items:center;justify-content:center;font-size:20px;line-height:1}
#clear.on{display:flex}
#count{position:absolute;right:46px;font-size:12px;color:var(--muted);pointer-events:none;
  max-width:120px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;display:none}
.chips{display:flex;gap:7px;overflow-x:auto;overflow-y:hidden;padding:8px 0 2px;
  scrollbar-width:none;-webkit-overflow-scrolling:touch}
.chips::-webkit-scrollbar{display:none}
.chip{flex:0 0 auto;min-height:34px;padding:6px 13px;border-radius:999px;border:1px solid var(--line);
  background:var(--surface2);color:var(--muted);font-size:14px;white-space:nowrap}
.chip.on{background:var(--accent);border-color:var(--accent);color:#fff;font-weight:600}
.chip.small{min-height:30px;padding:4px 11px;font-size:13px}
.bar{display:flex;align-items:center;justify-content:space-between;gap:8px;
  padding:10px 2px 8px;font-size:13px;color:var(--muted)}
.bar b{color:var(--text);font-weight:650}
#stat{flex:1 1 auto;min-width:0;line-height:1.5}
.link{flex:0 0 auto;white-space:nowrap;color:var(--accent);font-size:13px;
  padding:6px 2px;min-height:34px}
#famwrap{display:none}
#famwrap.on{display:flex}
.card{background:var(--surface);border:1px solid var(--line);border-radius:12px;
  margin-bottom:8px;box-shadow:var(--shadow);overflow:hidden}
.card-head{display:block;width:100%;text-align:left;padding:12px 12px 11px;min-height:56px}
.card-title{font-size:16px;font-weight:600;line-height:1.35;word-break:break-word;padding-right:26px;position:relative}
.card-title .arrow{position:absolute;right:0;top:1px;color:var(--muted);font-size:13px;font-weight:400}
.badges{display:flex;flex-wrap:wrap;gap:5px;margin-top:8px}
.tag,.fam,.warn{display:inline-block;font-size:11px;line-height:1.5;padding:2px 8px;border-radius:6px;
  background:var(--tb);color:var(--tf);white-space:nowrap;font-weight:500}
@media (prefers-color-scheme: dark){
  .tag{background:var(--tdb);color:var(--tdf)}
}
.fam{background:var(--surface2);color:var(--muted);border:1px solid var(--line)}
.warn{background:var(--warn-bg);color:var(--warn)}
.card-body{border-top:1px solid var(--line);background:var(--surface2);padding:4px 12px 10px}
.entry{padding:9px 0;border-bottom:1px dashed var(--line)}
.entry:last-child{border-bottom:0}
.entry-top{display:flex;flex-wrap:wrap;gap:5px;align-items:center;margin-bottom:6px}
.drv{display:flex;align-items:flex-start;gap:6px;flex-wrap:wrap;margin:5px 0}
.drv-label{font-size:12px;color:var(--muted);min-width:70px;padding-top:2px}
code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;font-size:13px;
  background:var(--surface);border:1px solid var(--line);border-radius:6px;padding:3px 7px;
  word-break:break-word;overflow-wrap:anywhere;flex:1 1 160px;min-width:0}
.panel li code{white-space:nowrap}
.copy{flex:0 0 auto;min-height:32px;padding:5px 10px;border-radius:8px;border:1px solid var(--line);
  background:var(--surface);color:var(--accent);font-size:12px}
.note,.orig{font-size:12px;color:var(--muted);margin-top:5px;word-break:break-word}
.cmdline{margin-top:9px;padding:8px 10px;border-radius:8px;background:var(--surface);
  border:1px solid var(--line);font-size:12px;color:var(--muted);word-break:break-all}
.cmdline code{border:0;background:none;padding:0;font-size:12px}
.more{display:block;width:100%;min-height:46px;margin:12px 0;border:1px solid var(--line);
  border-radius:11px;background:var(--surface);color:var(--accent);font-size:15px}
.empty{text-align:center;padding:42px 16px;color:var(--muted);font-size:14px}
.panel{background:var(--surface);border:1px solid var(--line);border-radius:12px;
  padding:12px;margin-bottom:10px;font-size:14px}
.panel h2{font-size:15px;margin:0 0 9px}
.panel p{margin:7px 0;color:var(--muted);font-size:13px}
.panel table{width:100%;border-collapse:collapse;font-size:13px}
.panel th,.panel td{text-align:left;padding:7px 4px;border-bottom:1px solid var(--line)}
.panel th{color:var(--muted);font-weight:500}
.panel td:last-child,.panel th:last-child{text-align:right}
.panel ul{margin:6px 0;padding-left:20px;color:var(--muted);font-size:13px}
.panel li{margin:5px 0}
.panel code{font-size:12px}
#top{position:fixed;right:16px;bottom:calc(20px + env(safe-area-inset-bottom));width:44px;height:44px;
  border-radius:50%;background:var(--accent);color:#fff;font-size:20px;display:none;
  align-items:center;justify-content:center;box-shadow:0 4px 14px rgba(0,0,0,.2);z-index:30}
#top.on{display:flex}
#toast{position:fixed;left:50%;transform:translateX(-50%);bottom:calc(78px + env(safe-area-inset-bottom));
  background:#111827;color:#fff;padding:9px 16px;border-radius:9px;font-size:13px;opacity:0;
  transition:opacity .2s;pointer-events:none;z-index:40;max-width:80vw;text-align:center}
#toast.on{opacity:1}
footer{text-align:center;color:var(--muted);font-size:12px;padding:8px 8px 20px;
  line-height:1.8;word-break:break-word;overflow-wrap:anywhere}
</style>
</head>
<body>
<header>
  <div class="hd">
    <div class="hd-row"><h1>打印机型号速查</h1><span class="sub">OpenWrt 打印驱动 · 离线可用</span></div>
    <div class="searchbox">
      <svg viewBox="0 0 24 24"><path d="M15.5 14h-.8l-.3-.3a6.5 6.5 0 1 0-.7.7l.3.3v.8l5 5 1.5-1.5-5-5zm-6 0a4.5 4.5 0 1 1 0-9 4.5 4.5 0 0 1 0 9z"/></svg>
      <input id="q" type="search" placeholder="搜型号或驱动名，如 1020 / P1006" autocomplete="off" autocapitalize="off" spellcheck="false">
      <span id="count"></span>
      <button id="clear" aria-label="清空">&times;</button>
    </div>
    <div class="chips" id="pkgs"></div>
    <div class="chips" id="quick"></div>
    <div class="chips" id="famwrap"></div>
  </div>
</header>
<div class="wrap">
  <div class="bar">
    <span id="stat"></span>
    <button class="link" id="togglePanels">总览与使用说明</button>
  </div>
  <div id="panels" hidden>
    <div class="panel" id="overview"></div>
    <div class="panel">
      <h2>怎么用</h2>
      <ul>
        <li>直接搜型号或驱动名，支持空格分隔多个关键词（如 <code>laserjet 1020</code>），忽略大小写和连字符。</li>
        <li>点击任一型号卡片展开，可看到该机型在哪些驱动包里、对应驱动名/备注，点「复制」可直接取用。</li>
        <li>顶部按驱动包筛选；选 gutenprint 时会出现家族筛选。搜索结果可用地址栏分享给别人。</li>
        <li>在设备上用 <code>lpinfo -m | grep -i 型号</code> 查看实际可用 PPD；本页数据来自仓库编译产物，仅供选型参考。</li>
      </ul>
    </div>
    <div class="panel">
      <h2>数据来源与口径</h2>
      <p id="source"></p>
      <p>EXPERIMENTAL 表示上游未充分实机验证，能装上但不保证所有分辨率/纸张组合可用。gutenprint 的驱动名即 <code>gutenprint.5.3://驱动名/expert</code> 中的型号段。</p>
    </div>
  </div>
  <div id="list"></div>
  <button class="more" id="more" hidden>加载更多</button>
  <div class="empty" id="empty" hidden>没有匹配的机型。<br>换个关键词，或点顶部「全部」清除筛选。</div>
  <footer id="foot"></footer>
</div>
<button id="top" aria-label="回到顶部">&#8593;</button>
<div id="toast"></div>
<script>
/*__INJECT__*/
(function(){
'use strict';
var PKGS=DATA.pkgs, FAMS=DATA.fams, ROWS=DATA.rows, META=DATA.meta, TAGCOL=DATA.colors;
var list=document.getElementById('list'), qEl=document.getElementById('q');
var pkg=-1, fam=-1, q='', shown=30, expanded=Object.create(null), results=[], timer=null;
var norm=function(s){return String(s).toLowerCase().replace(/[^a-z0-9\u4e00-\u9fff]+/g,'');};
var esc=function(s){return String(s).replace(/[&<>"']/g,function(c){
  return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});};
var tagStyle=function(p){var c=TAGCOL[p]||TAGCOL[5];
  return '--tb:'+c[0]+';--tf:'+c[1]+';--tdb:'+c[2]+';--tdf:'+c[3];};

/* 预建聚合组：同名（去标点/大小写后）机型合并，展开可看到全部驱动栈 */
var groups={}, order=[];
ROWS.forEach(function(r,i){
  var k=norm(r[2])||r[2].toLowerCase();
  if(!groups[k]){groups[k]={k:k,name:r[2],rows:[],names:{}};order.push(k);}
  groups[k].rows.push(i); groups[k].names[r[2]]=1;
});
var GROUPS=order.map(function(k){return groups[k];}).sort(function(a,b){
  return a.name.localeCompare(b.name,'en',{numeric:true});});
/* 各字段分别压缩、字段间留空格：避免 "1510"+"2.0.0" 拼成 "1510200" 误命中 "1020" */
var HAY=ROWS.map(function(r){
  var f=[r[2],r[3],r[4],PKGS[r[0]],r[1]>=0?FAMS[r[1]]:''].filter(Boolean);
  return [f.join(' ').toLowerCase(), f.map(function(x){return norm(x);}).join(' ')];
});
function rowMatch(i,terms){
  for(var t=0;t<terms.length;t++){
    var w=terms[t], c=norm(w), h=HAY[i];
    if(h[0].indexOf(w)<0 && (!c || h[1].indexOf(c)<0)) return false;
  }
  return true;
}
function compute(){
  var terms=(q||'').toLowerCase().split(/\s+/).filter(Boolean), out=[];
  for(var gi=0;gi<GROUPS.length;gi++){
    var g=GROUPS[gi], keep=[];
    for(var j=0;j<g.rows.length;j++){
      var i=g.rows[j], r=ROWS[i];
      if(pkg>=0 && r[0]!==pkg) continue;
      if(fam>=0 && r[1]!==fam) continue;
      if(terms.length && !rowMatch(i,terms)) continue;
      keep.push(i);
    }
    if(keep.length) out.push({g:g,rows:keep});
  }
  return out;
}
function tagHTML(p,n){return '<span class="tag" style="'+tagStyle(p)+'">'+esc(PKGS[p])+(n>1?' &times;'+n:'')+'</span>';}
function cardHTML(item){
  var g=item.g, open=!!expanded[g.k], byPkg={}, html='';
  item.rows.forEach(function(i){var p=ROWS[i][0];byPkg[p]=(byPkg[p]||0)+1;});
  html+='<article class="card"><button class="card-head" data-k="'+esc(g.k)+'" aria-expanded="'+open+'">';
  html+='<div class="card-title">'+esc(g.name)+'<span class="arrow">'+(open?'收起 &#9650;':'展开 &#9660;')+'</span></div>';
  html+='<div class="badges">';
  Object.keys(byPkg).sort().forEach(function(p){html+=tagHTML(+p,byPkg[p]);});
  if(item.rows.some(function(i){return ROWS[i][5];})) html+='<span class="warn">含 EXPERIMENTAL</span>';
  html+='</div></button>';
  if(open){
    html+='<div class="card-body">';
    item.rows.forEach(function(i){
      var r=ROWS[i], famName=r[1]>=0?FAMS[r[1]]:'';
      html+='<div class="entry"><div class="entry-top">'+tagHTML(r[0],1);
      if(famName) html+='<span class="fam">'+esc(famName)+'</span>';
      if(r[5]) html+='<span class="warn">EXPERIMENTAL</span>';
      html+='</div>';
      if(r[3]) html+='<div class="drv"><span class="drv-label">'+(r[0]===0?'驱动名':'驱动 / 备注')+'</span>'
        +'<code>'+esc(r[3])+'</code><button class="copy" data-copy="'+esc(r[3])+'">复制</button></div>';
      if(r[4]) html+='<div class="note">'+esc(r[4])+'</div>';
      if(Object.keys(g.names).length>1) html+='<div class="orig">原表型号：'+esc(r[2])+'</div>';
    });
    var cmd='lpinfo -m | grep -i "'+(q||g.name).replace(/"/g,'')+'"';
    html+='<div class="cmdline">设备查询命令 <code>'+esc(cmd)+'</code> '
      +'<button class="copy" data-copy="'+esc(cmd)+'">复制</button></div>';
    html+='</div>';
  }
  return html+'</article>';
}
function render(reset){
  results=compute();
  if(reset) shown=30;
  var slice=results.slice(0,shown), buf='';
  for(var i=0;i<slice.length;i++) buf+=cardHTML(slice[i]);
  list.innerHTML=buf;
  document.getElementById('more').hidden=slice.length>=results.length;
  document.getElementById('more').textContent='加载更多（还有 '+(results.length-slice.length)+' 款）';
  document.getElementById('empty').hidden=results.length>0;
  var recs=0; results.forEach(function(it){recs+=it.rows.length;});
  document.getElementById('stat').innerHTML='找到 <b>'+results.length+'</b> 款机型 · <b>'+recs+'</b> 条驱动记录';
  var cnt=document.getElementById('count');
  cnt.textContent=results.length?results.length+' 款':'无结果';
  cnt.style.display=q?'block':'none';
  document.getElementById('clear').className=q?'on':'';
  document.getElementById('quick').style.display=q?'none':'flex';
}
function chips(el,items,cur,cb){
  var b='';
  items.forEach(function(it,i){b+='<button class="chip'+(cur===i?' on':'')+'" data-i="'+i+'">'+esc(it[0])+'</button>';});
  el.innerHTML=b;
  el.onclick=function(e){var t=e.target.closest('[data-i]');if(!t)return;cb(+t.dataset.i);};
}
function renderPkgChips(){
  var items=[['全部']];
  PKGS.forEach(function(p,i){var n=0;ROWS.forEach(function(r){if(r[0]===i)n++;});items.push([p+' '+n,i]);});
  chips(document.getElementById('pkgs'),items,pkg>=0?pkg+1:0,function(i){
    pkg=i===0?-1:i-1; fam=-1;
    document.getElementById('famwrap').className=(pkg===0?'chips on':'chips');
    renderPkgChips(); render(true);
  });
  var fi=[['全部家族',-1]]; FAMS.forEach(function(f,i){fi.push([f,i]);});
  chips(document.getElementById('famwrap'),fi,fam>=0?fam+1:0,function(i){
    fam=fi[i][1]; renderPkgChips(); render(true);
  });
}
var QUICK=['HP LaserJet','HP OfficeJet','DeskJet','Brother','Canon','Epson','Samsung','Xerox','Kyocera','Ricoh','EXPERIMENTAL'];
chips(document.getElementById('quick'),
  QUICK.map(function(x){return [x,0];}),-1,function(i){
    qEl.value=QUICK[i]; q=QUICK[i]; syncHash(); render(true); window.scrollTo(0,0);
  });
var chipsEl=document.getElementById('quick');
Array.prototype.forEach.call(chipsEl.children,function(c){c.className='chip small';});
chipsEl.onclick=function(e){var t=e.target.closest('[data-i]');if(!t)return;
  qEl.value=QUICK[+t.dataset.i]; q=QUICK[+t.dataset.i]; syncHash(); render(true); window.scrollTo(0,0);};

function syncHash(){
  var h='q='+encodeURIComponent(q)+(pkg>=0?'&p='+pkg:'')+(fam>=0?'&f='+fam:'');
  try{history.replaceState(null,'','#'+h);}catch(e){location.hash=h;}
}
function readHash(){
  var s=location.hash.replace(/^#/,''); if(!s)return;
  s.split('&').forEach(function(kv){
    var p=kv.split('='), k=p[0], v=decodeURIComponent((p[1]||'').replace(/\+/g,' '));
    if(k==='q'){q=v;qEl.value=v;} else if(k==='p'&&+v>=0&&+v<PKGS.length){pkg=+v;}
    else if(k==='f'&&+v>=0&&+v<FAMS.length){fam=+v;}
  });
  document.getElementById('famwrap').className=(pkg===0?'chips on':'chips');
}
function toast(msg){
  var t=document.getElementById('toast'); t.textContent=msg; t.className='on';
  clearTimeout(t._t); t._t=setTimeout(function(){t.className='';},1600);
}
function copy(text){
  if(navigator.clipboard && window.isSecureContext){
    navigator.clipboard.writeText(text).then(function(){toast('已复制');},function(){fallbackCopy(text);});
  } else fallbackCopy(text);
}
function fallbackCopy(text){
  var ta=document.createElement('textarea'); ta.value=text;
  ta.style.cssText='position:fixed;top:-1000px;opacity:0';
  document.body.appendChild(ta); ta.select(); ta.setSelectionRange(0,text.length);
  var ok=false; try{ok=document.execCommand('copy');}catch(e){}
  document.body.removeChild(ta); toast(ok?'已复制':'复制失败，请长按选择');
}
qEl.addEventListener('input',function(){
  q=this.value; clearTimeout(timer);
  timer=setTimeout(function(){syncHash();render(true);},110);
});
document.getElementById('clear').onclick=function(){q='';qEl.value='';syncHash();render(true);qEl.focus();};
document.addEventListener('click',function(e){
  var c=e.target.closest('[data-copy]'); if(c){copy(c.dataset.copy);return;}
  var h=e.target.closest('.card-head'); if(h){var k=h.dataset.k;
    if(expanded[k])delete expanded[k];else expanded[k]=1; render(false); return;}
});
document.getElementById('more').onclick=function(){shown+=30;render(false);};
document.getElementById('togglePanels').onclick=function(){
  var p=document.getElementById('panels'); p.hidden=!p.hidden;
  this.textContent=p.hidden?'总览与使用说明':'收起说明';
};
document.getElementById('top').onclick=function(){window.scrollTo({top:0,behavior:'smooth'});};
window.addEventListener('scroll',function(){
  document.getElementById('top').className=window.scrollY>450?'on':'';
},{passive:true});
/* 总览 */
(function(){
  var counts=PKGS.map(function(_,p){var n=0;ROWS.forEach(function(r){if(r[0]===p)n++;});return n;});
  var byFam=FAMS.map(function(_,f){var n=0;ROWS.forEach(function(r){if(r[1]===f)n++;});return n;});
  var exp=0;ROWS.forEach(function(r){if(r[5])exp++;});
  var h='<h2>总览</h2><table><tr><th>驱动包</th><th>条目数</th></tr>';
  PKGS.forEach(function(p,i){h+='<tr><td>'+esc(p)+'</td><td>'+counts[i]+'</td></tr>';});
  h+='<tr><th>合计</th><th>'+ROWS.length+'</th></tr></table>';
  h+='<p>按名称聚合 '+GROUPS.length+' 组机型；原表跨栈去重口径为 <b>'+(META.unique||'—')
    +'</b> 款独立机型，其中 hplip 独占 <b>'+(META.exclusive||'—')+'</b> 款。标注 EXPERIMENTAL 的条目 '+exp+' 条。</p>';
  h+='<p>gutenprint 家族：'+FAMS.map(function(f,i){return esc(f)+' '+byFam[i];}).join(' · ')+'</p>';
  document.getElementById('overview').innerHTML=h;
  document.getElementById('source').textContent=META.source;
  document.getElementById('foot').innerHTML='共 '+ROWS.length+' 条驱动记录 · 生成于 '+esc(META.date)
    +'<br>数据来自 printer-models.md · 纯离线页面，可保存到手机';
})();
readHash(); renderPkgChips(); render(true);
})();
</script>
</body>
</html>
"""


def main():
    ap = argparse.ArgumentParser(description="从 printer-models.md 生成移动端单文件速查页")
    ap.add_argument("--src", help="Markdown 数据源，默认脚本目录或上级目录的 printer-models.md")
    ap.add_argument("--out", help="输出 HTML 路径，默认 output/printer-lookup/index.html")
    ap.add_argument("--copy", help="额外再写一份到该路径（默认写根目录 printer-models-mobile.html）")
    a = ap.parse_args()

    src = pathlib.Path(a.src) if a.src else (
        ROOT / "printer-models.md" if (ROOT / "printer-models.md").exists()
        else ROOT.parent / "printer-models.md"
    )
    out = pathlib.Path(a.out) if a.out else OUT_PAGE
    second = pathlib.Path(a.copy) if a.copy else (OUT_SINGLE if a.out is None else None)
    if not src.exists():
        print("缺少数据源:", src, file=sys.stderr)
        return 1
    text = src.read_text(encoding="utf-8")
    rows, families = parse_markdown(text)
    if not rows:
        print("解析结果为空，检查 Markdown 表格结构", file=sys.stderr)
        return 1

    stats = extract_stats(text)
    payload = {
        "pkgs": PKGS,
        "fams": FAMS,
        "rows": rows,
        "colors": TAG_COLORS,
        "meta": {
            "unique": stats["unique"],
            "exclusive": stats["exclusive"],
            "date": __import__("datetime").date.today().isoformat(),
            "source": (
                "型号数据来自 printer-models.md，提取自本仓库编译产物 ipk 内的驱动定义："
                "hplip/foo2zjs/splix 取 PPD 与 .drv；gutenprint 5.3.5 因 PPD 由驱动插件动态生成，"
                "取 /usr/share/gutenprint/5.3/xml/printers/*.xml 的 8 个家族定义。"
            ),
        },
    }
    js = (
        "var DATA="
        + json.dumps(payload, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")
        + ";"
    )
    page = TEMPLATE.replace("/*__INJECT__*/", js)
    def write_page(path, content):
        # 固定 LF：Windows 与 WSL 生成的页面字节一致，便于仓库复现
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
    out.parent.mkdir(parents=True, exist_ok=True)
    write_page(out, page)
    if second:
        second.parent.mkdir(parents=True, exist_ok=True)
        write_page(second, page)

    per_pkg = {p: sum(1 for r in rows if r[0] == i) for i, p in enumerate(PKGS)}
    print("解析条目:", len(rows), per_pkg)
    print("家族:", ", ".join(families))
    print("原表统计:", stats)
    print("页面大小:", out.stat().st_size, "bytes")
    print("输出:", out, ("及 " + str(second)) if second else "")
    return 0


if __name__ == "__main__":
    sys.exit(main())
