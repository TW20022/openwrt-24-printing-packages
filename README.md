# openwrt-24-printing-packages（合并版）

OpenWrt 24.10.8 `armsr/armv8` 打印软件包 feed，由两个上游仓库合并、去重并在 aarch64 交叉编译环境中全部实测编译通过。

## 一、来源与合并规则

| 来源 | 处理方式 |
|---|---|
| [woniuzfb/openwrt-24-printing-packages](https://github.com/woniuzfb/openwrt-24-printing-packages) | `hplip`（3.25.6，含 12 个本地补丁）、`python3-dbus`（1.4.0）保留此版本 |
| [TW20022/openwrt-24-printing-packages](https://github.com/TW20022/openwrt-24-printing-packages) | 其余全部包覆盖/新增（版本更新 + 新增打印机驱动与字体） |

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

**包清单（全部实测编译通过，共 39 个 ipk）**

| 包 | 版本 | 说明 |
|---|---|---|
| hplip / hplip-scan / hplip-ppds / hplip-tools | 3.25.6-r1 | HP 打印/扫描，主包 + 扫描库 + PPD + 命令行工具 |
| cups / libcups / libcupsimage | 2.4.20-r1 | CUPS 打印服务 |
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
| foomatic-filters | 4.0.17 | foomatic 过滤器 |
| cups-bjnp | 2.0.3-r1 | 佳能 BJNP 打印后端 |
| brlaser | 6-r1 | Brother 激光打印机驱动 |
| brhl3040cncupswrapper / brhl3040cnfilter | 1.0-r1 | Brother HL-3040CN 驱动 |
| foo2zjs | 20260206-r1 | 多品牌 GDI 打印机驱动（zjs/hp1020 等） |
| gutenprint-cups | 5.3.5-r1 | Gutenprint 驱动集合 |
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
CONFIG_PACKAGE_foo2zjs=y
CONFIG_PACKAGE_foomatic-filters=y
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

### 5. feeds 源与镜像
- `git.openwrt.org` 国内直连常在 `fetch-pack: unexpected disconnect` 处失败。解决办法：把 `feeds.conf` 里的官方 git 全部指向 GitHub 镜像并保留原 commit 锁定：
  ```
  src-git packages  https://gh-proxy.com/https://github.com/openwrt/packages.git^<commit>
  src-git luci      https://gh-proxy.com/https://github.com/openwrt/luci.git^<commit>
  src-git routing   https://gh-proxy.com/https://github.com/openwrt/routing.git^<commit>
  src-git telephony https://gh-proxy.com/https://github.com/openwrt/telephony.git^<commit>
  ```
- GitHub 直连不稳时统一用 `https://gh-proxy.com/https://github.com/...` 前缀（`git clone`、`wget`、raw 文件都适用）。

### 6. 配置与 make 目标的坑
- **子包 ≠ 编译目标**：`make package/liberation-fonts-ttf-LiberationMono/compile` 会报 `No rule to make target`。make 目标必须用**包目录名**（`package/feeds/printing/liberation-fonts/compile`），一个目录可含多个子包。
- **子包必须逐个启用**：hplip 有 4 个子包（hplip / hplip-scan / hplip-ppds / hplip-tools），`CONFIG_PACKAGE_hplip=y` 只产主包，扫描、PPD、`hp-setup` 命令行工具都在子包里。
- **符号名与目录名不一致**：`gutenprint` 的可选符号实际是 `CONFIG_PACKAGE_gutenprint-cups`；`liberation-fonts` 拆成 12 个 `-ttf-*` 子包；`ghostscript-gnu-gs-fonts` 只有 `-other` 一个可选子包。写错符号时 `make defconfig` 会静默丢弃，务必 `grep .config` 复查。
- **架构切换必须 `make dirclean`**：从 x86/64 切到 armsr/armv8 时，旧工具链和 build_dir 会污染结果。

### 7. Windows/WSL 环境（可选参考）
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
├── foomatic-filters/
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
└── README.md
```

## 六、已知限制

- `libImageProcessor` 相关功能（部分 LJZJet 系列）在 aarch64 上不可用。
- `ghostscript-gnu-gs-fonts-other`（额外字体）默认不启用。
- 编译验证环境为 4 核 / 3.8 GiB 内存，`-j2` 为稳妥值；内存 ≥8 GiB 可用 `-j$(nproc)` 提速。
