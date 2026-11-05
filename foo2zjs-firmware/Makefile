#
# Copyright (C) 2026 OpenWrt printing feed
#
# This is free software, licensed under the GNU General Public License v2.
#

include $(TOPDIR)/rules.mk

PKG_NAME:=foo2zjs-firmware
PKG_VERSION:=1.0
PKG_RELEASE:=1
PKG_LICENSE:=GPL-2.0
PKG_MAINTAINER:=openwrt-printing-feed

include $(INCLUDE_DIR)/package.mk

define Package/foo2zjs-firmware
  SECTION:=net
  CATEGORY:=Network
  TITLE:=Hotplug firmware loader for HP ZJS printers (foo2zjs)
  URL:=https://github.com/OpenPrinting/foo2zjs
  DEPENDS:=+foo2zjs +kmod-usb-printer
  PKGARCH:=all
endef

define Package/foo2zjs-firmware/description
  Loads HP LaserJet ZJS firmware (sihpXXXX.dl) into RAM-only printers
  (LJ 1000/1005/1018/1020, P1005/P1006/P1007/P1008/P1009, P1505)
  on USB hotplug. Firmware files are NOT shipped: HP licenses them for
  use with HP printers only. Copy your own .dl files to /lib/firmware/hp/.
endef

define Package/foo2zjs-firmware/conffiles
/etc/config/foo2zjs-fw
endef

define Build/Prepare
	mkdir -p $(PKG_BUILD_DIR)
endef

define Build/Compile
endef

define Package/foo2zjs-firmware/install
	$(INSTALL_DIR) $(1)/etc/hotplug.d/usb
	$(INSTALL_BIN) ./files/etc/hotplug.d/usb/20-foo2zjs-fw $(1)/etc/hotplug.d/usb/20-foo2zjs-fw

	$(INSTALL_DIR) $(1)/etc/config
	$(INSTALL_CONF) ./files/etc/config/foo2zjs-fw $(1)/etc/config/foo2zjs-fw

	$(INSTALL_DIR) $(1)/usr/sbin
	$(INSTALL_BIN) ./files/usr/sbin/foo2zjs-fw $(1)/usr/sbin/foo2zjs-fw

	$(INSTALL_DIR) $(1)/lib/firmware/hp
	$(INSTALL_DIR) $(1)/usr/share/foo2zjs-firmware
	$(INSTALL_DATA) ./files/README.firmware $(1)/usr/share/foo2zjs-firmware/README
endef

define Package/foo2zjs-firmware/postinst
#!/bin/sh
[ -n "$$IPKG_INSTROOT" ] && exit 0
mkdir -p /lib/firmware/hp
n=$$(ls /lib/firmware/hp/*.dl 2>/dev/null | wc -l)
if [ "$$n" -eq 0 ]; then
	echo "foo2zjs-firmware: /lib/firmware/hp/ is empty."
	echo "  Copy sihpXXXX.dl there, then run: foo2zjs-fw status"
	echo "  Firmware is HP-proprietary; it is not part of this package."
fi
exit 0
endef

$(eval $(call BuildPackage,foo2zjs-firmware))
