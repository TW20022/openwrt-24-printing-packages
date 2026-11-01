# openwrt-24-printing-packages（合并版）

OpenWrt 24.10.8 `armsr/armv8` 打印软件包 feed，由两个上游仓库合并、去重并在 aarch64 交叉编译环境中全部实测编译通过。

## 一、来源与合并规则

| 来源 | 处理方式 |
|---|---|
| [woniuzfb/openwrt-24-printing-packages](https://github.com/woniuzfb/openwrt-24-printing-packages) | `hplip`（3.25.6，含 12 个本地补丁）、`python3-dbus`（1.4.0）保留此版本 |
| TW20022 原 feed（已删除，内容并入本仓库） | 其余全部包覆盖/新增（版本更新 + 新增打印机驱动与字体） |

- `hplip` 采用 woniuzfb 3.25.6，因为 TW20022 的 hplip 是旧版 3.18.6，且 3.25.6 已在 aarch64 上验证通过（含禁用 x86 专用 libImageProcessor 的补丁）。
- 合并时保留各包自带的 `patches/` 目录，另有若干本地修复补丁（见第四节）。

## 二、软件与工具链版本

**编译环境**

| 项目 | 版本 |
|---|---|
| OpenWrt | v24.10.8（`git checkout v24.10.8`） |
| 目标平台 | `armsr/armv8`（`CONFIG_TARGET_BOARD="armsr"` / `CONFIG_TARGET_SUBTARGET="armv8"`） |
| 交叉工具链 | aarch64_generic，GCC 13.3.0，musl |
| 内核 | 6.6.144 |
| 构建主机 | Ubuntu 22.04 (WSL2)，4 vCPU / 3.8 GiB RAM |
| 包格式 | ipk（`aarch64_generic`） |

**包清单（全部实测编译通过，共 42 个 ipk）**

| 包 | 版本 | 说明 |
|---|---|---|
| hplip / hplip-scan / hplip-ppds / hplip-tools | 3.25.6-r1 | HP 打印/扫描，主包 + 扫描库 + PPD + 命令行工具 |
| cups / libcups / libcupsimage | 2.4.20-r1 | CUPS 打印服务（cupsd 守护进程 + libcups 库） |
| cups-client | 2.4.20-r1 | CUPS 客户端命令：`lp` `lpstat` `lpoptions` `cancel` `lpadmin` `lpinfo` `cupsfilter` `ipptool` `ippfind` |
| cups-bsd | 2.4.20-r1 | BSD 兼容命令：`lpr` `lpq` `lprm` `lpc` |
| cups-ppdc | 2.4.20-r1 | PPD 编译工具：`ppdc` `ppdi` `ppdmerge` `ppdpo` `ppdhtml`（可选） |
| cups-filters | 2.0.1-r1 | CUPS 过滤器 |
| libcupsfilters | 2.1.1-r1 | CUPS 过滤库 |
| libppd | 2.1.1-r1 | PPD 库 |
| ghostscript | 10.08.0-r1 | PostScript/PDF 解释器 |
| ghostscript-fonts-std | 8.11-r1 | 标准字体 |
| ghostscript-gnu-gs-fonts | 6.0（仅 `-other` 可选子包） | 额外字体（默认不选） |
| poppler | 25.09.1-r1 | PDF 渲染库 |
| qpdf | 12.4.2-r1 | PDF 处理 |
| lcms2 | 2.15-r1 | 色彩管理 |
| libcairo | 1.16.0-r2 | 2D 绘图库 |
| libjbigkit | 2.2-r1 | JBIG 图像压缩 |
| ~~foomatic-filters~~ | ~~4.0.17~~ | **已移除**：`foomatic-rip` 自 cups-filters 2.x 起已内置（见 `cups-filters` 的 `/usr/bin/foomatic-rip`、`/usr/lib/cups/filter/foomatic-rip`），独立包不再需要 |
| cups-bjnp | 2.0.3-r1 | 佳能 BJNP 打印后端 |
| brlaser | 6-r1 | Brother 激光打印机驱动 |
| brhl3040cncupswrapper / brhl3040cnfilter | 1.0-r1 / 1.0-r2 | Brother HL-3040CN 驱动（filter 为 i386 闭源程序，r2 起改为 box86 wrapper） |
| box86 | 0.3.9-r3 | i386 用户态模拟器（armhf 32 位 + Dynarec，随包附带 armhf / i386 glibc） |
| libarmeabi | 1.0-r1 | `libc.so.6` / `libm.so.6` 兼容垫片（指向 musl） |
| foo2zjs | 20260206-r1 | 多品牌 GDI 打印机驱动（zjs/hp1020 等） |
| gutenprint-cups | 5.3.5-r1 | Gutenprint 驱动集合（已关闭 simplified PPD，每个型号只列一条） |
| splix | 2.0.1-r1 | Samsung SPL 打印机驱动 |
| liberation-fonts-ttf-* | 2.1.5-r1 | Liberation 字体（12 个 ttf 子包） |
| python3-dbus | 1.4.0-r2 | hplip 依赖 |

## 三、编译方法

### 1. 准备环境

Ubuntu 22.04（本仓库在 WSL2 中构建）安装依赖：

```bash
sudo apt-get update
sudo apt-get install -y build-essential clang flex bison g++ gawk gcc-multilib g++-multilib \
  gettext git libncurses-dev libssl-dev python3-distutils rsync unzip zlib1g-dev file wget \
  xz-utils cpio python3 python3-pip python3-setuptools swig libelf-dev
```

### 2. 获取 OpenWrt 源码

```bash
git clone --depth 1 -b v24.10.8 https://github.com/openwrt/openwrt.git
cd openwrt
```

> 国内网络可把 GitHub 地址换成 `https://gh-proxy.com/https://github.com/...`。

### 3. 接入本 feed（必须放第一行）

```bash
cp feeds.conf.default feeds.conf
# 方式 A：本仓库为本地目录（推荐，改动即时生效）
sed -i '1i src-cpy printing /path/to/openwrt-printing-merged' feeds.conf
# 方式 B：直接引用 git 仓库
# sed -i '1i src-git printing https://gitee.com/<你的账号>/openwrt-24-printing-packages.git' feeds.conf
```

**feed 放第一行是强制的**：包名冲突时 feeds 按行序决定优先级，打印包必须优先于官方 packages feed（例如 `cups`、`poppler` 同名包）。

同时修正 pkgconf 的 cflags 透传（否则交叉编译时 cflags 被过滤，部分包 configure 失败）：

```bash
sed -i '/--keep-system-cflags\|--keep-system-libs/d' tools/pkgconf/files/pkg-config
```

### 4. 基础配置

```bash
# 以官方 armsr/armv8 的 buildinfo 作为基线配置
wget https://downloads.openwrt.org/releases/24.10.8/targets/armsr/armv8/config.buildinfo -O .config

# 启用需要的打印包
cat >> .config <<'EOF'
CONFIG_PACKAGE_hplip=y
CONFIG_PACKAGE_hplip-scan=y
CONFIG_PACKAGE_hplip-ppds=y
CONFIG_PACKAGE_hplip-tools=y
CONFIG_PACKAGE_cups=y
CONFIG_PACKAGE_cups-client=y
CONFIG_PACKAGE_cups-bsd=y
CONFIG_PACKAGE_cups-ppdc=y
CONFIG_PACKAGE_cups-filters=y
CONFIG_PACKAGE_ghostscript=y
CONFIG_PACKAGE_poppler=y
CONFIG_PACKAGE_qpdf=y
CONFIG_PACKAGE_lcms2=y
CONFIG_PACKAGE_libcairo=y
CONFIG_PACKAGE_libcupsfilters=y
CONFIG_PACKAGE_libppd=y
CONFIG_PACKAGE_python3-dbus=y
CONFIG_PACKAGE_cups-bjnp=y
CONFIG_PACKAGE_brlaser=y
CONFIG_PACKAGE_brhl3040cncupswrapper=y
CONFIG_PACKAGE_brhl3040cnfilter=y
CONFIG_PACKAGE_box86=y
CONFIG_PACKAGE_libarmeabi=y
CONFIG_PACKAGE_foo2zjs=y
# 注意：不需要 foomatic-filters —— cups-filters 2.x 已内置 foomatic-rip
CONFIG_PACKAGE_ghostscript-fonts-std=y
CONFIG_PACKAGE_gutenprint-cups=y
CONFIG_PACKAGE_libjbigkit=y
CONFIG_PACKAGE_splix=y
EOF

make defconfig
./scripts/feeds update -a
./scripts/feeds install -a
```

### 5. 分阶段编译（低内存主机务必降低并行度）

```bash
make -j2 toolchain/compile V=s      # 工具链
make -j2 target/compile V=s         # 内核与基础系统
make -j2 package/hplip/compile V=s  # 单个包调试

# 批量编译整个打印组（目标按包目录名，不能按子包名）
for d in /path/to/openwrt-printing-merged/*/; do
  echo "package/feeds/printing/$(basename $d)/compile"
done | xargs make -j2 V=s
```

产物：`bin/packages/aarch64_generic/printing/*.ipk`

### 6. 安装到设备

```bash
opkg update
opkg install *.ipk
hp-plugin -i     # 安装 HP 专有插件
hp-setup -i      # 连接打印机后配置
```

## 四、编译过程中踩过的坑

### 1. hplip：`cannot find -lImageProcessor`（aarch64 链接失败）★
- **现象**：`hpcups` 链接报 `skipping incompatible ./prnt/hpcups/libImageProcessor.so`，`Error 1`。
- **原因**：HP 只随源码分发 **x86/x86_64 预编译**的 `libImageProcessor.so`，无 aarch64 版本、无源码。
- **修复**：`hplip/patches/012-disable-imageprocessor-aarch64.patch` —— `hpcups_CXXFLAGS` 增加 `-DDISABLE_IMAGEPROCESSOR`、`hpcups_LDADD` 去掉 `-lImageProcessor`、`install-data-hook` 阻止拷贝 x86 库。源码中所有调用点都有该宏保护，仅 LJZJet（`ljzjstream`）路径使用，普通打印机不受影响。
- **复核结论（aarch64 实测，2026-10）**：补丁只改 `Makefile.am` 一行，`#ifdef DISABLE_IMAGEPROCESSOR` 分支是 HP 上游自带的。实测 hpcups 在此宏下仍能为 LJ 1020 产出**合法 ZJS 流**（`ESC E` + `@PJL ENTER LANGUAGE=ZJS` + `JZJZ` 魔数 + 数据块），编码路径未被打断。判别方法见 7.5「离线验证 ZJS 编码器」。

### 2. 低内存主机 OOM（`cc1plus: Killed`）
- **现象**：编译 `tools/llvm-bpf` 时 g++ 被杀，`toolchain/compile Error 2`。
- **原因**：3.8 GiB 内存 + `-j4` 编 LLVM/clang 大文件内存耗尽。
- **修复**：改 `-j1/-j2`；并**关闭 BPF/LLVM 工具链**（hplip 不需要）：
  ```
  # CONFIG_BPF_TOOLCHAIN_BUILD_LLVM is not set
  CONFIG_BPF_TOOLCHAIN_NONE=y
  # CONFIG_USE_LLVM_BUILD is not set
  ```
  注意 `CONFIG_USE_LLVM_BUILD` 才是 `tools/Makefile` 里的真正开关。

### 3. foo2zjs：`all-test Error 1`（构建机缺 `gs` / `dc`）
- **现象**：`Makefile:398: all-test Error 1`，提示 "gs is not installed"。
- **原因**：`all-test` 检测**构建主机**是否装了 ghostscript / GNU dc，用于本地生成测试页；交叉编译主流程并不需要。
- **修复**：`foo2zjs/patches/003-skip-host-gs-dc-check.patch`，把 `@if ! type gs`、`@if ! type dc`、`@if ! dc -V` 三处检查改为 `@if false`。

### 4. gutenprint 5.3.5：`Error 127`（host 工具路径失效）★★
- **现象 A**：`xml-stamp` 阶段执行 `build_dir/hostpkg/gutenprint-5.3.5/src/xml/printers/check_duplicate_printers.test`，报 No such file。
- **现象 B**：`xmli18n-tmp.h` 阶段执行 `build_dir/hostpkg/.../src/xml/extract-strings`，同样 127。
- **原因**：feed Makefile 用 SED 把目标树里的 `./check_duplicate_printers.test`、`./extract-strings` 改写为 **hostpkg 构建目录的绝对路径**；但 host 阶段完成后 OpenWrt host-build 机制会 `find | xargs rm -rf` 清空 hostpkg 构建目录（只留 stamp），目标编译时这些路径必然不存在。
- **修复**：注释掉 `check_duplicate_printers.test` 那条 SED（目标树 `--disable-test` 下本来就有本地 stub）；`extract-strings` 那条 SED 的替换目标改为 `true`（`xmli18n-tmp.h` 只在 dist 期生成 `po/POTFILES.in` 用，`--disable-nls` 下全树无人 include）。

### 5. gutenprint：CUPS 里每个型号出现两条（`Simplified` 不是"简体中文"）★
- **现象**：CUPS「添加打印机」的型号列表里，同一个打印机出现两份，其中一份名称后缀是 `Simplified`，容易被误认为是"简体中文"。
- **真相**：这是 gutenprint 的**简化版 PPD**（选项精简，给新手用），与语言无关。源码 `gutenprint.c: list_ppds()` 对每个型号固定输出 `/expert` 一条，若编译时定义了 `GENERATE_SIMPLIFIED_PPDS` 再额外输出 `/simple` 一条，两条的 CUPS 语言字段都硬编码为 `"en"`：
  ```c
  printf("\"%s://%s/expert\" ... \"%s\"", scheme, driver, "en", ...);
  #ifdef GENERATE_SIMPLIFIED_PPDS
  printf("\"%s://%s/simple\" ... \"%s" VERSION " Simplified\"", ...);
  #endif
  ```
- **触发条件**：feed Makefile 里的 `--enable-simplified-cups-ppds`（对应 `BUILD_SIMPLE_PPDS=-DGENERATE_SIMPLIFIED_PPDS`）。
- **修复**：改为 `--disable-simplified-cups-ppds`，重编后驱动二进制里只剩 `/expert"`、不再有 `/simple"`，CUPS 列表每个型号只出现一条。
- **附注**：本 feed 的 gutenprint 包**不打包任何 PPD**（`install` 段故意不拷 `/usr/share/cups/model`），PPD 由 `gutenprint.5.3` 驱动 / `cups-genppd.5.3` 在运行时生成；型号名来自 XML，官方明确要求型号名不翻译，因此列表显示为英文属正常。

### 6. feeds 源与镜像
- `git.openwrt.org` 国内直连常在 `fetch-pack: unexpected disconnect` 处失败。解决办法：把 `feeds.conf` 里的官方 git 全部指向 GitHub 镜像并保留原 commit 锁定：
  ```
  src-git packages  https://gh-proxy.com/https://github.com/openwrt/packages.git^<commit>
  src-git luci      https://gh-proxy.com/https://github.com/openwrt/luci.git^<commit>
  src-git routing   https://gh-proxy.com/https://github.com/openwrt/routing.git^<commit>
  src-git telephony https://gh-proxy.com/https://github.com/openwrt/telephony.git^<commit>
  ```
- GitHub 直连不稳时统一用 `https://gh-proxy.com/https://github.com/...` 前缀（`git clone`、`wget`、raw 文件都适用）。

### 7. 配置与 make 目标的坑
- **子包 ≠ 编译目标**：`make package/liberation-fonts-ttf-LiberationMono/compile` 会报 `No rule to make target`。make 目标必须用**包目录名**（`package/feeds/printing/liberation-fonts/compile`），一个目录可含多个子包。
- **子包必须逐个启用**：hplip 有 4 个子包（hplip / hplip-scan / hplip-ppds / hplip-tools），`CONFIG_PACKAGE_hplip=y` 只产主包，扫描、PPD、`hp-setup` 命令行工具都在子包里。
- **符号名与目录名不一致**：`gutenprint` 的可选符号实际是 `CONFIG_PACKAGE_gutenprint-cups`；`liberation-fonts` 拆成 12 个 `-ttf-*` 子包；`ghostscript-gnu-gs-fonts` 只有 `-other` 一个可选子包。写错符号时 `make defconfig` 会静默丢弃，务必 `grep .config` 复查。
- **架构切换必须 `make dirclean`**：从 x86/64 切到 armsr/armv8 时，旧工具链和 build_dir 会污染结果。

### 8. Windows/WSL 环境（可选参考）
- 本机为 Windows Server 2022（build 20348），内置 `wsl.exe` 只是引导器（不支持 `--import`），WSL 3.x 安装包不支持 Server 2022（exit 83），改用 **WSL 2.7.14 MSI** 后正常。
- WSL 功能启用后必须**重启**才能生效。
- 在 Git Bash 里调用 `msiexec` / `dism` 会被 MSYS 路径转换破坏参数，改用 PowerShell 或 `MSYS_NO_PATHCONV=1`。

## 五、目录结构

```
.
├── brhl3040cncupswrapper/     # 各打印包目录，每个含 Makefile 与可选 patches/
├── brhl3040cnfilter/
├── brlaser/
├── cups/
├── cups-bjnp/
├── cups-filters/
├── foo2zjs/patches/003-skip-host-gs-dc-check.patch
├── ghostscript/
├── ghostscript-fonts-std/
├── ghostscript-gnu-gs-fonts/
├── gutenprint/               # Makefile 内含本地修复（见 4.4）
├── hplip/patches/            # 001~012，含 012-disable-imageprocessor-aarch64.patch
├── lcms2/
├── liberation-fonts/
├── libcairo/
├── libcupsfilters/
├── libjbigkit/
├── libppd/
├── poppler/
├── python3-dbus/
├── qpdf/
├── splix/
├── cups-zh/                  # CUPS Web 中文界面包（非 OpenWrt 包，见 7.9）
└── README.md
```

## 六、已知限制

- `libImageProcessor` 相关功能（部分 LJZJet 系列）在 aarch64 上不可用。
- **`foomatic-filters` 已从本 feed 移除**：cups-filters 2.x 自带 `foomatic-rip`（`/usr/bin/foomatic-rip` 与 `/usr/lib/cups/filter/foomatic-rip`），独立包冗余；且 TW20022 版该包缺少 `install` 段，OpenWrt 会以 `package has no install section` 跳过、根本不产出 ipk。
- `ghostscript-gnu-gs-fonts-other`（额外字体）默认不启用。
- 编译验证环境为 4 核 / 3.8 GiB 内存，`-j2` 为稳妥值；内存 ≥8 GiB 可用 `-j$(nproc)` 提速。

## 七、路由器端安装与使用

### 7.1 安装顺序

```sh
opkg update
opkg install cups cups-filters ghostscript qpdf poppler      # 打印底座
opkg install hplip hplip-ppds hplip-tools                    # hplip 三件套（主包会自动拉依赖）
opkg install hplip-scan                                      # 需要扫描时再装（引入 libsane）
```

包体参考：`hplip` 9.4 MB（装在设备上约 16 MB）、`hplip-ppds` 17 MB（1370 个 PPD，空间紧张可只解压需要的型号）、`hplip-tools` 0.5 MB。

### 7.2 启动服务并添加打印机

```sh
/etc/init.d/cupsd enable && /etc/init.d/cupsd start
hp-probe -b usb                       # 列出 USB 上的 HP 设备
hp-makeuri <bus>:<dev>                # 取得设备 URI，如 hp:/usb/HP_LaserJet_1020?serial=000000000WA...
hp-setup -i                          # 交互式建队列（无 GUI，务必带 -i）
```

`hp-setup -i` 会依次询问：连接方式（usb）→ 型号 → PPD → 队列名，最后自动调用 CUPS 接口创建队列。也可以直接在 CUPS 网页 `http://<路由器IP>:631` 或 LuCI 的「网络打印机」里添加，设备 URI 填 `hp-makeuri` 给出的那一串（网页管理需先配好管理员与访问控制，见 7.8）。

### 7.3 hplip-tools 里有什么

`hplip-tools` 提供 37 个命令，常用：

| 命令 | 用途 |
|---|---|
| `hp-setup` | 建队列（`-i` 交互模式） |
| `hp-plugin` | 安装 HP 专有插件（GDI 机型必需，见 7.5） |
| `hp-firmware` | 手动给设备刷固件（`-y3 -s <bus>:<dev>` 静默） |
| `hp-probe` / `hp-makeuri` | 探测设备 / 生成设备 URI |
| `hp-info` / `hp-levels` | 设备信息 / 墨粉余量 |
| `hp-check` / `hp-doctor` | 依赖与配置自检 |
| `hp-clean` / `hp-align` / `hp-testpage` | 清洗 / 校准 / 测试页 |
| `hp-config_usb_printer` | 热插拔时被调用，内部做插件检测 + 固件下发 |

### 7.4 USB 热插拔脚本做了什么

`/etc/hotplug.d/usb/10-hp-printer`（主包自带，`conffiles` 保护）在 USB `bind` 事件时：

1. 只处理 HP 设备（`PRODUCT` 前缀 `3f0/`）且接口类为 `07/01`（打印机类）；
2. 关闭该设备的 USB autosuspend（避免打印中途休眠掉线）；
3. 给 `/dev/lpX` 设 `root:nogroup 0664`；
4. 若 `/var/lib/hp/hplip.state` 不存在且 `~/.hplip/plugin_tmp/installPlugin.py` 在，则执行插件安装（本 feed 的 `010-fix-hplip-plugin-install.patch` 支持这种预解压安装）；
5. 调 `hp-config_usb_printer <BUSNUM>:<DEVNUM>`——**这一步才是决定要不要刷固件的地方**。

### 7.5 GDI / 主机型打印机（LaserJet 1020、P1005 等）的固件问题

> **实测设备修正**：本 feed 实际测试机是 **HP LaserJet 3050**（`03f0:3217`，MFP，标准 PCL5 机型），`models.dat` 里 `plugin=0`、`fw-download=False`，插上即枚举为 `1-1:1.0 class=07`（printer）+ `1-1:1.1 class=ff`（扫描件），**既不装插件也不刷固件**，`hp-setup -i` 直接建队列就能打。先确认自己的机型属于哪一类：
>
> ```sh
> sed -n '/^\[hp_laserjet_1020\]/,/^\[/p' /usr/share/hplip/data/models/models.dat | grep -E 'plugin|fw-download'
> # plugin=0 → 到此为止；plugin=1 + fw-download=True 才是下面要折腾的机型
> ```

这类机器（1000/1005/1018/1020/1022、P1005/P1006/P1007/P1008/P1009/P1505、P1102/P1566 等）是"无固件裸机"：冷启动后 USB 里只有引导程序，**必须先下发固件才会变成正常打印机**，断电后每次都要重来。

- 数据侧标记：`models.dat` 里这些型号是 `plugin=1`、`plugin-reason=1`、`fw-download=True`。
- 固件不在 hplip 包里：本 feed 的 `hplip` ipk **0 个固件文件**（`data/` 下只有 ldl/localization/models/pcl/ps）。
- 固件只在 HP 专有插件里：`hplip-3.25.6-plugin.run`（11.5 MB，SHA256 `0cd770036532a2d706c0f449ee1e3ef9b4de7b6cea5aaf2e76fe2da3f97f6ffc`）内含 13 个 `*.fw.gz`，其中 `hp_laserjet_1020.fw.gz` 仅 70 KB、`hp_laserjet_p1005.fw.gz` 153 KB。

**结论：需要装一次插件，但不需要每次手动刷固件。**

`hp-config_usb_printer` 的逻辑（`config_usb_printer.py`）：先查插件状态，未安装则打印
`HP Device plugin's are not installed. Please install plugin's using hp-plugin command.` 并跳过；
已安装且 `fw-download=True` 才执行 `hp-firmware -y3 -s <busnum>:<devnum>`（**三位补零的 USB ID**，来自 `lsusb`，不是 sysfs 的 `1-1:1.0`）自动下发。因此在热插拔脚本生效之前，必须先满足插件这一环。

插件安装（二选一）：

```sh
# A. 联网：直接让 hp-plugin 下载（需访问 hplip.sf.net / openprinting.org）
hp-plugin -i

# B. 离线：把 hplip-3.25.6-plugin.run 传到路由器后指定路径安装
hp-plugin -i -p /tmp/hplip-3.25.6-plugin.run

# B'. 离线且不想装 32 MB 插件的"只放固件"做法（够 1020/P1005 打印用）
mkdir -p /usr/share/hplip/data/firmware
cp hp_laserjet_1020.fw.gz /usr/share/hplip/data/firmware/
hp-config_usb_printer 001:004       # 或 hp-firmware -y3 -s 001:004（busnum:devnum）
```

> 说明：本 feed 编译时 `hpijs-install=no`、只保留 hpcups，LJ 1020 这类 ZJS 机型的编码器在 hpcups 内（`LJZjStream.cpp`），所以插件对它们的主要作用就是**携带固件**，用 B' 即可；`bb_*` 后端与扫描插件才需要完整插件。

**装插件踩过的两个坑**

1. `error: Plug-in GPG file [.../plugin.run.asc] download failed` —— `-p` 指定本地 `.run` 时，hp-plugin 会去找**同目录同名**的 `.asc`。缺 `.asc` 只是警告，随后问 `Do you still want to install the plug-in? (y=yes, n=no*, q=quit)`，**默认 no，必须手动敲 `y`**。
2. `error: GPG command not found` —— 补上 `.asc` 反而卡死（OpenWrt 没有 `gnupg`，`hp-plugin` 2.1 也没有跳过验签的开关）。正确做法是**把 `.asc` 挪走**退回第 1 条，用 sha256 代替验签：
   ```sh
   sha256sum /tmp/hplip-3.25.6-plugin.run   # 应等于 0cd7700...7f6ffc
   mv /tmp/hplip-3.25.6-plugin.run.asc /tmp/plugin.run.asc.bak
   hp-plugin -i -p /tmp/hplip-3.25.6-plugin.run
   ```
   若 `~/.hplip/plugin_tmp/` 已有上次解压结果，会跳过解压直接 `Executing installPlugin.py` → `Done.`（没有 license 提示），属正常。

**装成功长什么样**

```sh
ls -l /usr/share/hplip/data/firmware/*.fw.gz   # 13 个：1000/1005_series/1018/1020/P1005~P1009/P1505/P1102/P1102w/P1566
ls /root/.hplip/plugin_tmp/*.so | head         # bb_escl-arm64.so 等 aarch64 后端在
```

**坑三：`/var` 是 tmpfs，插件状态随重启丢失** ★★

状态文件落在 `/var/lib/hp/hplip.state`（`/var` 软链到 `/tmp`），内容三行 `[plugin]` / `installed = 1` / `eula = 1` / `version = 3.25.6`。断电即丢，表现为"插件装过、但每次冷启动还得手动刷固件"。修复：复制到 `/etc` 再软链回去，并让 `rc.local` 在 tmpfs 重建后补链：

```sh
mkdir -p /etc/hplip && cp /var/lib/hp/hplip.state /etc/hplip.state && chmod 644 /etc/hplip.state
rm -f /var/lib/hp/hplip.state && ln -s /etc/hplip.state /var/lib/hp/hplip.state
sed -i '/^exit 0/i [ -e /var/lib/hp/hplip.state ] || { mkdir -p /var/lib/hp; ln -sf /etc/hplip.state /var/lib/hp/hplip.state; }' /etc/rc.local
```

**离线验证 ZJS 编码器（没有 1020 硬件也能做）★**

`hp-laserjet_1020.ppd.gz` 的 `cupsFilter` 是 `application/vnd.cups-raster 0 hpcups`，手动跑两段过滤器就能拿到真实打印数据流（绕开 cupsd 和 `file:` 后端的限制）：

```sh
cd /tmp
printf '%%!PS\n/Helvetica findfont 20 scalefont setfont 72 700 moveto (test) show showpage\n' > page.ps
zcat /usr/share/ppd/HP/hp-laserjet_1020.ppd.gz > p1020.ppd
export PPD=/tmp/p1020.ppd CUPS_DATADIR=/usr/share/cups
/usr/lib/cups/filter/gstoraster 1 root page 1 "PageSize=A4 Resolution=600dpi" page.ps > page.raster 2>gs.err
/usr/lib/cups/filter/hpcups     1 root page 1 "PageSize=A4 Resolution=600dpi" page.raster > h.zjs 2>hpc.err
ls -l page.raster h.zjs; cat hpc.err; hexdump -C -n 48 h.zjs
```

实测三组数据（aarch64，`DISABLE_IMAGEPROCESSOR` 生效，单页 A4 600dpi）：

| 页面内容 | `x.raster` | `hpcups` 产出 | `foo2zjs` 产出 |
|---|---|---|---|
| 实心黑块（`rectfill`） | 3941714 | **503 B** | — |
| 一行文字 + 一条线 | 3941714 | **1495 B** | — |
| 5000 条随机短线（噪点） | 3941714 | **8791 B** | **9371 B** |

判读要点：

- `raster` 体积恒定（3941714）是因为它这个配置下是**未压缩定长位图**（621 B/行 × 6347 行），只由页面尺寸决定，**不能用来看内容**。
- ZJS 是**行间差分**编码，所以纯色页反而最小（行间差分≈0），文字页中等、噪点页最大——**体积随内容复杂度单调增长**，说明编码器真的在编码。
- 噪点页 hpcups 8791 B vs foo2zjs 9371 B，仅差 6%，与已知正确实现同量级 → **hpcups 的 ZJS 路径在 aarch64 上可用**。

判据：0 字节、或 `hpc.err` 提到 `ImageProcessor`、或噪点页仍在 1 KB 级 → 编码器不可用，改走 7.6 的 foo2zjs。正常时 `hpc.err` 只有 `PAGE: 1 1`。

噪点页比纯色页更能暴露问题，验证时优先用它。`foo2zjs` 的参考值来自其 PPD 的 `FoomaticRIPCommandLine`（`foo2zjs-wrapper -z1 -P -L0 %A`）：

```sh
cat > noise.ps <<'EOF'
%!PS-Adobe-3.0
0 setlinewidth
1 1 5000 { pop rand 500 mod 40 add rand 780 mod 40 add moveto rand 100 mod 8 add 0 rlineto stroke } for
showpage
EOF
foo2zjs-wrapper -z1 -P -L0 noise.ps > noise_f.zjs 2> f.err
```

附注：`gstoraster` 单独运行时**退出会 SIGSEGV**（raster 已完整写出，CUPS 管线内实测不影响出纸）。

### 7.6 另一条路：foo2zjs（全开源，已在本 feed 内）

> 定位说明：本 feed 的 hpcups 已实测能为 LJ 1020 产出合法 ZJS 流（见 7.5），**正常情况下不需要切到这条路**；foo2zjs 作为"hpcups 输出异常"或"不想装 HP 专有插件"时的备选。

`foo2zjs` ipk 自带 `HP-LaserJet_1020.ppd.gz` 与固件转换工具 `arm2hpdl`，同样支持 1005/1018/1020/1022/P1005/P1006/P1505 等。但它**不带固件本体**（`sihp1020.dl` 需要自行获取），安装后需自建 hotplug 规则把 `.dl` 写进 `/dev/usb/lp0`。适合不想引入 HP 专有插件的场景。

### 7.7 Brother 三个包怎么用

| 包 | 内容 | 适用 |
|---|---|---|
| `brlaser` v6 | 全开源 CUPS filter `rastertobrlaser` + `brlaser.drv` | Brother 激光/LED 打印机（HL-1110/1210W/L2300D/L2340DW/L2360DN、DCP-1510/1600/7030/7055/7060D/7080/L2500D/L2520D/L2540DW、MFC-1910W 等约 29 个型号） |
| `brhl3040cnfilter` | Brother 官方 **i386 闭源** filter + LUT 色彩表（从 hl3040cnlpr-1.1.2-1.i386.deb 重打包） | 仅 Brother HL-3040CN |
| `brhl3040cncupswrapper` | 本 feed 重编译的 aarch64 CUPS filter + PPD | 仅 Brother HL-3040CN |

**安装后在 CUPS「添加打印机」里可见吗？可见（需本 feed 2024-10-30 之后的版本）：**

- `brlaser` 装完即把 `brlaser.drv` 装进 `/usr/share/cups/drv/`，CUPS 的 `lpinfo -m` / 添加打印机列表会直接列出全部 29 个型号（早期版本漏装 drv，只能 `lpadmin -P` 手动指定 PPD，已修复）；
- `brhl3040cncupswrapper` 装完会把 PPD 同时放到 `/usr/share/ppd/hl3040cn.ppd` 和 `/usr/share/cups/model/brother/hl3040cn.ppd.gz`，后者在 CUPS 添加打印机列表中显示为 "Brother HL3040CN"。

**HL-3040CN 的数据流与注意点：**

```
CUPS → brhl3040cncupswrapper(aarch64，写 /tmp/brparam.rc、/tmp/brpaper.inf)
     → exec /opt/brother/Printers/hl3040cn/brhl3040cnfilter(i386 闭源)
     → 打印机
```

- aarch64 上跑 i386 filter 依赖 `box86` + `libarmeabi`，**本 feed 已提供这两个包**（`box86` 为 armhf 32 位 + Dynarec，随包附带 armhf 与 i386 两套 glibc；`libarmeabi` 提供 `/lib/libc.so.6`、`/lib/libm.so.6` 垫片），opkg 会自动带上依赖。
- 前提：内核必须开启 `CONFIG_COMPAT`（AArch32 兼容层）。验证：`/opt/brother/Printers/hl3040cn/brhl3040cnfilter` 能打印 `Error: invalid option !!` 即整链正常；若报 `Exec format error` 说明内核未开 32 位兼容。
- `box86 -v` 会打印两行 `sh: lscpu: not found`，这是 box86 探测 CPU 型号时调用 `lscpu` 产生的噪声，无害可忽略。
- 二选一即可：HL-3040CN 优先试 `brlaser`？不行——brlaser 不含 3040CN，这个型号只能走官方 filter 路线。

**通用建队命令（两包通吃）：**

```sh
opkg install brlaser                       # 或 brhl3040cnfilter brhl3040cncupswrapper
lpinfo -m | grep -i brother                # 确认驱动已可见
lpadmin -p Brother -v usb:///dev/usb/lp0 -m everywhere && lpadmin -p Brother -E   # 或:
lpadmin -p HL3040CN -v usb:///dev/usb/lp0 -P /usr/share/ppd/hl3040cn.ppd -E
```

### 7.8 CUPS 网页管理：管理员账号、关掉强制 HTTPS、放开内网段

**为什么会跳到 https / 报 `Upgrade Required`（426）**

CUPS 2.2 起对 `<Location /admin>` 默认要求加密，浏览器用 `http://<IP>:631/admin` 会被重定向到 `https://<IP>:631/admin`，而 cupsd 用的是自签证书，于是继续报证书错误，管理页永远进不去。要两处同时成立才不跳：

1. `cupsd.conf` 顶层 `DefaultEncryption Never`
2. 各 `<Location>` 里不能有 `Encryption Required`（有就删掉或改成 `IfRequested`）

**"管理员"是谁：CUPS 没有自己的账号库**

它用**系统账号 + `SystemGroup`**（写在 `cups-files.conf`）判定：只有属于 `SystemGroup` 所列组的用户才能进 `/admin`。上游 Linux 默认是 `lpadmin` 组，**OpenWrt 没有这个组**，所以默认任何账号都进不去。

```sh
grep -n SystemGroup /etc/cups/cups-files.conf
grep -E '^(lpadmin|cupsadmin):' /etc/group
```

两种做法：

```sh
# 做法 A：直接用 root 登录（最省事）
# cups-files.conf 里改成：SystemGroup root
# 前提：root 已设密码（passwd root），且 cupsd 以 root 运行（能读 /etc/shadow，OpenWrt 默认如此）

# 做法 B：建专用管理员（推荐，不动 root）
addgroup -S cupsadmin
adduser  -S -D -H -G cupsadmin -s /bin/false cupsadmin
passwd cupsadmin
# cups-files.conf 里改成：SystemGroup sys root cupsadmin
```

**cupsd.conf 需要的块**（先 `cp /etc/cups/cupsd.conf /etc/cups/cupsd.conf.bak`）

```apache
Listen 0.0.0.0:631              # 原来若是 localhost:631，外网段根本连不上
Listen /var/run/cups/cups.sock  # 保留：本机 CLI 走 socket 免密码
WebInterface Yes                # 打开网页管理
DefaultAuthType Basic
DefaultEncryption Never         # ★ 关键：不再强制跳 https

<Location />
  Order allow,deny
  Allow 127.0.0.1
  Allow 192.168.0.0/16
  Allow 10.0.0.0/8
  Allow 172.16.0.0/12
</Location>

<Location /admin>
  AuthType Default
  Require user @SYSTEM          # 只有 SystemGroup 成员可进
  Order allow,deny
  Allow 127.0.0.1
  Allow 192.168.0.0/16
  Allow 10.0.0.0/8
  Allow 172.16.0.0/12
</Location>

<Location /admin/conf>
  AuthType Default
  Require user @SYSTEM
  Order allow,deny
  Allow 127.0.0.1
  Allow 192.168.0.0/16
  Allow 10.0.0.0/8
  Allow 172.16.0.0/12
</Location>
```

上面三个网段覆盖了绝大多数家用/办公内网，**按实际 LAN 改成一条**（如 `Allow 192.168.1.0/24`）更严谨。`Allow @LOCAL` 也可以，但它只认"直连网段"，路由器桥接/容器场景经常判不出来，所以这里写死网段更可靠。

**生效与验证**

```sh
cupsd -t                       # 语法检查，必须先过
/etc/init.d/cupsd restart
grep -n Encryption /etc/cups/cupsd.conf   # 除 DefaultEncryption Never 外不应再有 Encryption 行
curl -sI http://127.0.0.1:631/admin | head -1
# 期望：HTTP/1.1 401 Unauthorized   （要求认证＝正常）
# 若是 426 Upgrade Required → 还有 Encryption Required 没清干净
```

浏览器访问 `http://<路由器IP>:631/admin`，弹出认证框时输入 `cupsadmin`（做法 B）或 `root`（做法 A）＋密码，即可进入 Administration。

**注意点**

- `DefaultEncryption Never` + Basic 认证 = 密码以 base64 明文过网，**只在内网用**，绝不要把 631 映射到 WAN；防火墙默认也不放行 WAN→631，不需要额外动作。
- 本机 root 跑 `lpadmin` / `hp-setup` 走 `/var/run/cups/cups.sock`，由 socket 对端身份自动认证，**完全不需要网页登录**——建队列这条主线可以完全不碰 web 管理。
- 若登录一直失败，先确认 cupsd 是否带 PAM：`strings /usr/sbin/cupsd | grep -c pam_`。命中但 `/etc/pam.d/cupsd` 不存在时，认证会始终失败；此时退回"只用 CLI 管理"，或改用 `SystemGroup root`（无 PAM 时 CUPS 直接读 `/etc/shadow` 比对）。
- 给客户端共享打印机（IPP）：`lpadmin` 建好队列后，其他机器用 `ipp://<路由器IP>:631/printers/<队列名>` 添加即可，不需要开 `Browsing`。

### 7.9 CUPS Web 界面中文化

Web 管理界面（`http://<路由器IP>:631`）的页面由 `/usr/share/cups/templates/*.tmpl` 渲染，CGI 直接读文件，**覆盖即生效**，与浏览器 `Accept-Language`、`DefaultLanguage` 都无关。首页 `/` 则是静态文件 `doc-root/index.html`，与模板是两套东西，缺一个就会出现「首页叫类别、内页叫类」这类不一致。

本仓库 `cups-zh/` 目录是这套中文界面包（含 `cups-zh-cn.tar.gz` 成品包）：

| 内容 | 说明 |
|---|---|
| `cups-zh-cn.tar.gz` | 20 KB，65 个中文模板 + 中文首页 + `install.sh` |
| `templates/` | 同上，未打包的源文件，便于对比与二次修改 |
| `doc-root/index.html` | 中文首页 |
| `install.sh` | 安装 / `--restore` 还原英文 |
| `README.md` | 译文来源、逐项修补清单、已知限制 |

安装：

```sh
# 把 cups-zh-cn.tar.gz 传到路由器
cd /tmp && tar xzf cups-zh-cn.tar.gz && cd cups-zh-cn && sh install.sh
# 装完 Ctrl+F5 强刷，浏览器会缓存模板渲染结果
sh install.sh --restore        # 想回英文
```

脚本会自动做完这些事（不需要手动指定路径）：

1. 探测 `DocumentRoot`：先看 `cups-files.conf` 里未注释的 `DocumentRoot`，没有就按 `cups.css` 实际位置反推。**OpenWrt 的 cups 把 doc-root 装在 `/usr/share/doc/cups`**，而 `/usr/share/cups/` 下根本没有 `doc-root`，写死路径必然扑空。
2. 英文原件备份到 `/usr/share/cups/templates/default.en/`，首页备份为 `index.html.en`。
3. 按本机 `header.tmpl` 判断用 `.header` 还是 `.cups-header` 类名——CUPS 2.4 系列中途改过类名，用错会让导航栏丢样式。
4. 只覆盖本机真实存在的模板（上游已删的旧模板自动跳过），装完列出「本机有、包里没有」的英文模板。
5. 重启 `cupsd`。

相对上游译文做的修补（详见 `cups-zh/README.md`）：

- `printer-added.tmpl` 补回「设置打印机选项」表单（`org.cups.sid` 全缺，否则加完打印机没有下一步入口）；
- `jobs.tmpl` 补回 `{job_hold_until=auth-info-required?}` 分支，译全 `pending since / completed at / Unknown / Withheld`；
- 导航「类别」「类」统一为**集群**，删掉「帮助」（`/help/` 文档未随固件打包，点了必 404）；class 相关 10 个模板的「添加类/删除类/修改类」同步改为集群；
- 首页正文原来整片是 `help/*.html` 死链，换成「常用入口」+「使用提示」两栏。

已知限制：`opkg upgrade cups` 会覆盖模板，升级后需重跑一次 `install.sh`；`help/` 在线帮助文档未汉化（原始译文包也没做完，几 MB 放路由器 Flash 不划算）。
