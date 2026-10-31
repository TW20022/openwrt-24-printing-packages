# OpenWrt 24.10 printing feed 支持的打印机型号清单

依据：编译产物 ipk 内附带的 PPD/drv 文件（aarch64_generic 实测内容）

## 总览

| 驱动包 | 去重型号数 | 覆盖品牌 | 数据来源 |
|---|---|---|---|
| hplip (hplip-ppds) | 1296 | HP / Apollo | 1370 个 PPD |
| foo2zjs | 101 | HP/Oki/Samsung/KONICA/Xerox/Minolta/Fuji Xerox/Ricoh/Kyocera/Epson/Dell/Lexmark 等 | 101 个 PPD |
| splix | 86 | Samsung/Xerox/Dell/Toshiba/Lexmark | 246 个 PPD（多语言重复） |
| brlaser | 29 | Brother | brlaser.drv（动态生成 PPD） |
| brhl3040cnfilter/cupswrapper | 1 | Brother HL-3040CN（彩色 LED） | 专用闭源 filter（i386，经 box86） |

---

## hplip — 1296 个型号

Apollo 2100, hpcups 3.25.6
Apollo 2150, hpcups 3.25.6
Apollo 2200, hpcups 3.25.6
Apollo 2500, hpcups 3.25.6
Apollo 2600, hpcups 3.25.6
Apollo 2650, hpcups 3.25.6
Apollo p2000-u, hpcups 3.25.6
Apollo p2250, hpcups 3.25.6
HP 2000c, hpcups 3.25.6
HP 2500c, hpcups 3.25.6
HP 910, hpcups 3.25.6
HP 915, hpcups 3.25.6
HP Amp, hpcups 3.25.6
HP Business Inkjet 1000, hpcups 3.25.6
HP Business Inkjet 1100, hpcups 3.25.6
HP Business Inkjet 1200, hpcups 3.25.6
HP Business Inkjet 2200, hpcups 3.25.6
HP Business Inkjet 2230, hpcups 3.25.6
HP Business Inkjet 2250 PS - Ver 1.6 Postscript (recommended)
HP Business Inkjet 2250 pcl3, hpcups 3.25.6
HP Business Inkjet 2280 PS - v1.0 Postscript (recommended)
HP Business Inkjet 2280 pcl3, hpcups 3.25.6
HP Business Inkjet 2300 PS v3010.107 Postscript (recommended)
HP Business Inkjet 2300 pcl3, hpcups 3.25.6
HP Business Inkjet 2600 PS -RC-2.0 Postscript (recommended)
HP Business Inkjet 2600 pcl3, hpcups 3.25.6
HP Business Inkjet 2800 PS v3010.107 Postscript (recommended)
HP Business Inkjet 2800 pcl3, hpcups 3.25.6
HP Business Inkjet 3000 PS - RC1.1 Postscript (recommended)
HP Business Inkjet 3000 pcl3, hpcups 3.25.6
HP CM8050 CM8060 Color MFP with Edgeline Technology Postscript (recommended)
HP Color Inkjet Printer cp1700, hpcups 3.25.6
HP Color LaserJet 1600, hpcups 3.25.6, requires proprietary plugin
HP Color LaserJet 2500 Series, hpcups 3.25.6
HP Color LaserJet 2500 v3010.107 Postscript (recommended)
HP Color LaserJet 2550 Series Postscript (recommended)
HP Color LaserJet 2600n, hpcups 3.25.6, requires proprietary plugin
HP Color LaserJet 2605 Postscript (recommended)
HP Color LaserJet 2700 Postscript (recommended)
HP Color LaserJet 2800 Series Postscript (recommended)
HP Color LaserJet 3000 Postscript (recommended)
HP Color LaserJet 3000 pcl3, hpcups 3.25.6
HP Color LaserJet 3500, hpcups 3.25.6, requires proprietary plugin
HP Color LaserJet 3500n, hpcups 3.25.6, requires proprietary plugin
HP Color LaserJet 3550, hpcups 3.25.6, requires proprietary plugin
HP Color LaserJet 3550n, hpcups 3.25.6, requires proprietary plugin
HP Color LaserJet 3600, hpcups 3.25.6, requires proprietary plugin
HP Color LaserJet 3700 Postscript (recommended)
HP Color LaserJet 3700 pcl3, hpcups 3.25.6
HP Color LaserJet 3700n, hpcups 3.25.6
HP Color LaserJet 3800 Postscript (recommended)
HP Color LaserJet 3800 pcl3, hpcups 3.25.6
HP Color LaserJet 4500 pcl3, hpcups 3.25.6
HP Color LaserJet 4500 v2014.200 Postscript (recommended)
HP Color LaserJet 4550 pcl3, hpcups 3.25.6
HP Color LaserJet 4550 v3010.107 Postscript (recommended)
HP Color LaserJet 4600 pcl3, hpcups 3.25.6
HP Color LaserJet 4600 v3010.107 Postscript (recommended)
HP Color LaserJet 4610 Postscript (recommended)
HP Color LaserJet 4610 pcl3, hpcups 3.25.6
HP Color LaserJet 4650 Postscript (recommended)
HP Color LaserJet 4650 pcl3, hpcups 3.25.6
HP Color LaserJet 4700 Postscript (recommended)
HP Color LaserJet 4700 pcl3, hpcups 3.25.6
HP Color LaserJet 4730mfp Postscript (recommended)
HP Color LaserJet 4730mfp pcl3, hpcups 3.25.6
HP Color LaserJet 5, hpcups 3.25.6
HP Color LaserJet 5/5M v2015.104 Postscript (recommended)
HP Color LaserJet 5500 pcl3, hpcups 3.25.6
HP Color LaserJet 5500 v3010.107 Postscript (recommended)
HP Color LaserJet 5550 pcl3, hpcups 3.25.6
HP Color LaserJet 5550 v3010.107 Postscript (recommended)
HP Color LaserJet 5700 Postscript (recommended)
HP Color LaserJet 5m pcl3, hpcups 3.25.6
HP Color LaserJet 6700 Postscript (recommended)
HP Color LaserJet 6701 Postscript (recommended)
HP Color LaserJet 8500 Postscript (recommended)
HP Color LaserJet 8500 pcl3, hpcups 3.25.6
HP Color LaserJet 8550 Postscript (recommended)
HP Color LaserJet 8550 pcl3, hpcups 3.25.6
HP Color LaserJet 9500 MFP Postscript (recommended)
HP Color LaserJet 9500 Postscript (recommended)
HP Color LaserJet 9500 pcl3, hpcups 3.25.6
HP Color LaserJet CM1015 Postscript (recommended)
HP Color LaserJet CM1312 MFP Series Postscript (recommended)
HP Color LaserJet CM2320 MFP Series Postscript (recommended)
HP Color LaserJet CM3530 MFP Postscript (recommended)
HP Color LaserJet CM4540 MFP Postscript (recommended)
HP Color LaserJet CM4730 MFP Postscript (recommended)
HP Color LaserJet CM6030 MFP Postscript (recommended)
HP Color LaserJet CM6040 MFP Postscript (recommended)
HP Color LaserJet CM6049 MFP Postscript (recommended)
HP Color LaserJet CP1510 Series Postscript (recommended)
HP Color LaserJet CP2020 Series Postscript (recommended)
HP Color LaserJet CP2020 Series with Duplexer Postscript (recommended)
HP Color LaserJet CP3505 Postscript (recommended)
HP Color LaserJet CP3525 Postscript (recommended)
HP Color LaserJet CP4005 Postscript (recommended)
HP Color LaserJet CP4020-CP4520 Series Postscript (recommended)
HP Color LaserJet CP5220 Series Postscript (recommended)
HP Color LaserJet CP5220 Series with Duplexer Postscript (recommended)
HP Color LaserJet CP5520 Series Postscript (recommended)
HP Color LaserJet CP6015 Postscript (recommended)
HP Color LaserJet E45028 Postscript (recommended)
HP Color LaserJet E55040 Postscript (recommended)
HP Color LaserJet E65050 E65060 Postscript (recommended)
HP Color LaserJet E65150 E65160 Postscript (recommended)
HP Color LaserJet E67550 E67560 Postscript (recommended)
HP Color LaserJet E67650 E67660 Postscript (recommended)
HP Color LaserJet E75245 Postscript (recommended)
HP Color LaserJet E85055 Postscript (recommended)
HP Color LaserJet Enterprise M750 Postscript (recommended)
HP Color LaserJet Flow 5800 Postscript (recommended)
HP Color LaserJet Flow 6800 Postscript (recommended)
HP Color LaserJet Flow E57540 Postscript (recommended)
HP Color LaserJet Flow MFP M680 Postscript (recommended)
HP Color LaserJet Flow X579 Postscript (recommended)
HP Color LaserJet Flow X57945 Postscript (recommended)
HP Color LaserJet Flow x580 Postscript (recommended)
HP Color LaserJet FlowMFP M578 Postscript (recommended)
HP Color LaserJet FlowMFP M776 Postscript (recommended)
HP Color LaserJet M455 Postscript (recommended)
HP Color LaserJet M552 Postscript (recommended)
HP Color LaserJet M553 Postscript (recommended)
HP Color LaserJet M554 Postscript (recommended)
HP Color LaserJet M555 Postscript (recommended)
HP Color LaserJet M651 Postscript (recommended)
HP Color LaserJet M652 M653 Postscript (recommended)
HP Color LaserJet M751 Postscript (recommended)
HP Color LaserJet M855 Postscript (recommended)
HP Color LaserJet M856 Postscript (recommended)
HP Color LaserJet MFP 5800 Postscript (recommended)
HP Color LaserJet MFP 6800 Postscript (recommended)
HP Color LaserJet MFP 6801 Postscript (recommended)
HP Color LaserJet MFP E47528 Postscript (recommended)
HP Color LaserJet MFP E57540 Postscript (recommended)
HP Color LaserJet MFP E77422 Postscript (recommended)
HP Color LaserJet MFP E77428 Postscript (recommended)
HP Color LaserJet MFP E78223 Postscript (recommended)
HP Color LaserJet MFP E78228 Postscript (recommended)
HP Color LaserJet MFP E785 Postscript (recommended)
HP Color LaserJet MFP E78523 Postscript (recommended)
HP Color LaserJet MFP E78528 Postscript (recommended)
HP Color LaserJet MFP M480 Postscript (recommended)
HP Color LaserJet MFP M577 Postscript (recommended)
HP Color LaserJet MFP M578 Postscript (recommended)
HP Color LaserJet MFP M680 Postscript (recommended)
HP Color LaserJet MFP M681 M682 Postscript (recommended)
HP Color LaserJet MFP M776 Postscript (recommended)
HP Color LaserJet MFP X677 Postscript (recommended)
HP Color LaserJet MFP X67755 Postscript (recommended)
HP Color LaserJet MFP X67765 Postscript (recommended)
HP Color LaserJet Pro 4201 Postscript (recommended)
HP Color LaserJet Pro M252 Postscript (recommended)
HP Color LaserJet Pro M452 Postscript (recommended)
HP Color LaserJet Pro M453-4 Postscript (recommended)
HP Color LaserJet Pro M478f-9f Postscript (recommended)
HP Color LaserJet Pro M479 Postscript (recommended)
HP Color LaserJet Pro MFP M274 Postscript (recommended)
HP Color LaserJet Pro MFP M277 Postscript (recommended)
HP Color LaserJet Pro MFP M377 Postscript (recommended)
HP Color LaserJet Pro MFP M476 Postscript (recommended)
HP Color LaserJet Pro MFP M477 Postscript (recommended)
HP Color LaserJet Pro MFP M481 Postscript (recommended)
HP Color LaserJet Pro MFP m176n, hpcups 3.25.6, requires proprietary plugin
HP Color LaserJet Pro MFP m177fw, hpcups 3.25.6
HP Color LaserJet X557 Postscript (recommended)
HP Color LaserJet X654 Postscript (recommended)
HP Color LaserJet X65455 Postscript (recommended)
HP Color LaserJet X65465 Postscript (recommended)
HP Color LaserJet cm1312 MFP pcl3, hpcups 3.25.6
HP Color LaserJet cm1312nfi MFP pcl3, hpcups 3.25.6
HP Color LaserJet cm2320 MFP pcl3, hpcups 3.25.6
HP Color LaserJet cm2320fxi MFP pcl3, hpcups 3.25.6
HP Color LaserJet cm2320n MFP pcl3, hpcups 3.25.6
HP Color LaserJet cm2320nf MFP pcl3, hpcups 3.25.6
HP Color LaserJet cm3530 MFP pcl3, hpcups 3.25.6
HP Color LaserJet cm4540 MFP pcl3, hpcups 3.25.6
HP Color LaserJet cm4730 MFP pcl3, hpcups 3.25.6
HP Color LaserJet cm6030 MFP pcl3, hpcups 3.25.6
HP Color LaserJet cm6040 MFP, hpcups 3.25.6
HP Color LaserJet cm6049 MFP, hpcups 3.25.6
HP Color LaserJet cp1215, hpcups 3.25.6, requires proprietary plugin
HP Color LaserJet cp1217, hpcups 3.25.6
HP Color LaserJet cp1514n pcl3, hpcups 3.25.6
HP Color LaserJet cp1515n pcl3, hpcups 3.25.6
HP Color LaserJet cp1518ni pcl3, hpcups 3.25.6
HP Color LaserJet cp2025 pcl3, hpcups 3.25.6
HP Color LaserJet cp2025dn pcl3, hpcups 3.25.6
HP Color LaserJet cp2025n pcl3, hpcups 3.25.6
HP Color LaserJet cp2025x pcl3, hpcups 3.25.6
HP Color LaserJet cp3505 pcl3, hpcups 3.25.6
HP Color LaserJet cp3525 pcl3, hpcups 3.25.6
HP Color LaserJet cp4005 pcl3, hpcups 3.25.6
HP Color LaserJet cp4020 Series pcl3, hpcups 3.25.6
HP Color LaserJet cp4520 Series pcl3, hpcups 3.25.6
HP Color LaserJet cp5225 pcl3, hpcups 3.25.6
HP Color LaserJet cp5225dn pcl3, hpcups 3.25.6
HP Color LaserJet cp5225n pcl3, hpcups 3.25.6
HP Color LaserJet cp5520 Series pcl3, hpcups 3.25.6
HP Color LaserJet cp6015 pcl3, hpcups 3.25.6
HP Color LaserJet flow MFP M880 Postscript (recommended)
HP Color LaserJet v2013.114 Postscript (recommended)
HP Color MFP 8801 Postscript (recommended)
HP Color MFP E78323-25-30 Postscript (recommended)
HP Color MFP E786-25-30-35 Postscript (recommended)
HP Color MFP E78625-30-35 Postscript (recommended)
HP Color MFP E877-40-50-60-70 Postscript (recommended)
HP Color MFP E87740-50-60-70 Postscript (recommended)
HP ColorLaserJet M153-M154 Postscript (recommended)
HP ColorLaserJet M155-M156 Postscript (recommended)
HP ColorLaserJet M253-M254 Postscript (recommended)
HP ColorLaserJet M255-M256 Postscript (recommended)
HP ColorLaserJet MFP M178-M181 Postscript (recommended)
HP ColorLaserJet MFP M182-M185 Postscript (recommended)
HP ColorLaserJet MFP M278-M281 Postscript (recommended)
HP ColorLaserJet MFP M282-M285 Postscript (recommended)
HP DesignJet T1530ps PS3
HP DesignJet T1600 PS3
HP DesignJet T1600dr PS3
HP DesignJet T1700 - PS Postscript (recommended)
HP DesignJet T1700dr - PS Postscript (recommended)
HP DesignJet T1708 - PS Postscript (recommended)
HP DesignJet T1708dr - PS Postscript (recommended)
HP DesignJet T2530ps PS3
HP DesignJet T2600 PS3
HP DesignJet T2600dr PS3
HP DesignJet T930 - PostScript
HP DesignJet XL 3600 PS3
HP DesignJet XL 3800 MFP PS - PostScript
HP DesignJet Z2600 PostScript - PS
HP DesignJet Z5600 PostScript - PS
HP DesignJet Z6 24in - PS Postscript (recommended)
HP DesignJet Z6 44in - PS Postscript (recommended)
HP DesignJet Z6 Pro 64in - PS Postscript (recommended)
HP DesignJet Z6610ps 60in - PS Postscript (recommended)
HP DesignJet Z6810ps 42in - PS Postscript (recommended)
HP DesignJet Z6810ps 60in - PS Postscript (recommended)
HP DesignJet Z6dr 44in - PS Postscript (recommended)
HP DesignJet Z9 24in - PS Postscript (recommended)
HP DesignJet Z9 44in - PS Postscript (recommended)
HP DesignJet Z9 Pro 64in - PS Postscript (recommended)
HP DesignJet Z9dr 44in - PS Postscript (recommended)
HP Designjet 4000ps Postscript (recommended)
HP Designjet 4020ps Postscript (recommended)
HP Designjet 4500mfp Postscript (recommended)
HP Designjet 4500ps Postscript (recommended)
HP Designjet 4520mfp Postscript (recommended)
HP Designjet 4520ps Postscript (recommended)
HP Designjet D5800ps Postscript (recommended)
HP Designjet T1100ps 24in Postscript (recommended)
HP Designjet T1100ps 44in Postscript (recommended)
HP Designjet T1120ps 24in Postscript (recommended)
HP Designjet T1120ps 44in Postscript (recommended)
HP Designjet T1200 PostScript
HP Designjet T1300 PostScript
HP Designjet T1500 - PostScript
HP Designjet T2300 PostScript
HP Designjet T2500 - PostScript
HP Designjet T3500ps Postscript (recommended)
HP Designjet T7100ps Monochrome Postscript (recommended)
HP Designjet T7100ps Postscript (recommended)
HP Designjet T7200ps Postscript (recommended)
HP Designjet T770ps 24in Postscript (recommended)
HP Designjet T770ps 44in Postscript (recommended)
HP Designjet T790ps 24in Postscript (recommended)
HP Designjet T790ps 44in Postscript (recommended)
HP Designjet T795ps 44in Postscript (recommended)
HP Designjet T920 PostScript
HP Designjet Z5200 PostScript - PS
HP Designjet Z5400 PostScript - PS
HP Designjet Z6100ps 42in Photo Postscript (recommended)
HP Designjet Z6100ps 60in Photo Postscript (recommended)
HP Designjet Z6200ps 42in Photo Postscript (recommended)
HP Designjet Z6200ps 60in Photo Postscript (recommended)
HP Designjet Z6600ps Postscript (recommended)
HP Designjet Z6800ps Photo Postscript (recommended)
HP Deskjet 1000 j110 Series, hpcups 3.25.6
HP Deskjet 1010 Series, hpcups 3.25.6
HP Deskjet 1050 j410 Series, hpcups 3.25.6
HP Deskjet 1100, hpcups 3.25.6
HP Deskjet 1110 Series, hpcups 3.25.6
HP Deskjet 1120, hpcups 3.25.6
HP Deskjet 1125, hpcups 3.25.6
HP Deskjet 1200 Series, hpcups 3.25.6
HP Deskjet 1200c, hpcups 3.25.6
HP Deskjet 1220c, hpcups 3.25.6
HP Deskjet 1280, hpcups 3.25.6
HP Deskjet 1510 Series, hpcups 3.25.6
HP Deskjet 1600c, hpcups 3.25.6
HP Deskjet 1600cm, hpcups 3.25.6
HP Deskjet 1600cn, hpcups 3.25.6
HP Deskjet 2000 j210 Series, hpcups 3.25.6
HP Deskjet 2020 Series, hpcups 3.25.6
HP Deskjet 2050 j510 Series, hpcups 3.25.6
HP Deskjet 2130 Series, hpcups 3.25.6
HP Deskjet 2200 Series, hpcups 3.25.6
HP Deskjet 2300 Series, hpcups 3.25.6
HP Deskjet 2510 Series, hpcups 3.25.6
HP Deskjet 2520 Series, hpcups 3.25.6
HP Deskjet 2540 Series, hpcups 3.25.6
HP Deskjet 2600 Series, hpcups 3.25.6
HP Deskjet 2640 Series, hpcups 3.25.6
HP Deskjet 2700 Series, hpcups 3.25.6
HP Deskjet 2800 Series, hpcups 3.25.6, requires proprietary plugin
HP Deskjet 3000 j310 Series, hpcups 3.25.6
HP Deskjet 3050 j610 Series, hpcups 3.25.6
HP Deskjet 3050a j611 Series, hpcups 3.25.6
HP Deskjet 3070 b611 Series, hpcups 3.25.6
HP Deskjet 3320, hpcups 3.25.6
HP Deskjet 3325, hpcups 3.25.6
HP Deskjet 3420, hpcups 3.25.6
HP Deskjet 3425, hpcups 3.25.6
HP Deskjet 3450, hpcups 3.25.6
HP Deskjet 350, hpcups 3.25.6
HP Deskjet 3500, hpcups 3.25.6
HP Deskjet 3510 Series, hpcups 3.25.6
HP Deskjet 3520 Series, hpcups 3.25.6
HP Deskjet 3540 Series, hpcups 3.25.6
HP Deskjet 3550, hpcups 3.25.6
HP Deskjet 3600, hpcups 3.25.6
HP Deskjet 3630 Series, hpcups 3.25.6
HP Deskjet 3650, hpcups 3.25.6
HP Deskjet 3700 Series, hpcups 3.25.6
HP Deskjet 3740, hpcups 3.25.6
HP Deskjet 3810, hpcups 3.25.6
HP Deskjet 3816, hpcups 3.25.6
HP Deskjet 3819, hpcups 3.25.6
HP Deskjet 3820, hpcups 3.25.6
HP Deskjet 3822, hpcups 3.25.6
HP Deskjet 3830 Series, hpcups 3.25.6
HP Deskjet 3840, hpcups 3.25.6
HP Deskjet 3870, hpcups 3.25.6
HP Deskjet 3900, hpcups 3.25.6
HP Deskjet 3910, hpcups 3.25.6
HP Deskjet 3920, hpcups 3.25.6
HP Deskjet 3940, hpcups 3.25.6
HP Deskjet 400, hpcups 3.25.6
HP Deskjet 400l, hpcups 3.25.6
HP Deskjet 4100 Series, hpcups 3.25.6
HP Deskjet 4200 Series, hpcups 3.25.6, requires proprietary plugin
HP Deskjet 450, hpcups 3.25.6
HP Deskjet 4510 Series, hpcups 3.25.6
HP Deskjet 4530 Series, hpcups 3.25.6
HP Deskjet 460, hpcups 3.25.6
HP Deskjet 4610 Series, hpcups 3.25.6
HP Deskjet 4620 Series, hpcups 3.25.6
HP Deskjet 4640 Series, hpcups 3.25.6
HP Deskjet 4670 Series, hpcups 3.25.6
HP Deskjet 4720 Series, hpcups 3.25.6
HP Deskjet 4800 Series, hpcups 3.25.6
HP Deskjet 4900 Series, hpcups 3.25.6, requires proprietary plugin
HP Deskjet 500, hpcups 3.25.6
HP Deskjet 5000 Series, hpcups 3.25.6
HP Deskjet 500c, hpcups 3.25.6
HP Deskjet 505j, hpcups 3.25.6
HP Deskjet 510, hpcups 3.25.6
HP Deskjet 5100, hpcups 3.25.6
HP Deskjet 520, hpcups 3.25.6
HP Deskjet 5200 Series, hpcups 3.25.6
HP Deskjet 540, hpcups 3.25.6
HP Deskjet 5400 Series, hpcups 3.25.6
HP Deskjet 550c, hpcups 3.25.6
HP Deskjet 5520 Series, hpcups 3.25.6
HP Deskjet 5550, hpcups 3.25.6
HP Deskjet 5551, hpcups 3.25.6
HP Deskjet 5552, hpcups 3.25.6
HP Deskjet 5570 Series, hpcups 3.25.6
HP Deskjet 5600, hpcups 3.25.6
HP Deskjet 5640 Series, hpcups 3.25.6
HP Deskjet 5650, hpcups 3.25.6
HP Deskjet 5652, hpcups 3.25.6
HP Deskjet 5700, hpcups 3.25.6
HP Deskjet 5730 Series, hpcups 3.25.6
HP Deskjet 5800, hpcups 3.25.6
HP Deskjet 5810 Series, hpcups 3.25.6
HP Deskjet 5820 Series, hpcups 3.25.6
HP Deskjet 5850, hpcups 3.25.6
HP Deskjet 5900 Series, hpcups 3.25.6
HP Deskjet 600, hpcups 3.25.6
HP Deskjet 610c, hpcups 3.25.6
HP Deskjet 610cl, hpcups 3.25.6
HP Deskjet 6120, hpcups 3.25.6
HP Deskjet 6122, hpcups 3.25.6
HP Deskjet 6127, hpcups 3.25.6
HP Deskjet 612c, hpcups 3.25.6
HP Deskjet 630c, hpcups 3.25.6
HP Deskjet 632c, hpcups 3.25.6
HP Deskjet 640c, hpcups 3.25.6
HP Deskjet 648c, hpcups 3.25.6
HP Deskjet 6500, hpcups 3.25.6
HP Deskjet 6520 Series, hpcups 3.25.6
HP Deskjet 656c, hpcups 3.25.6
HP Deskjet 660, hpcups 3.25.6
HP Deskjet 6600, hpcups 3.25.6
HP Deskjet 670, hpcups 3.25.6
HP Deskjet 670c, hpcups 3.25.6
HP Deskjet 670tv, hpcups 3.25.6
HP Deskjet 672c, hpcups 3.25.6
HP Deskjet 680, hpcups 3.25.6
HP Deskjet 6800, hpcups 3.25.6
HP Deskjet 682, hpcups 3.25.6
HP Deskjet 690c, hpcups 3.25.6
HP Deskjet 692, hpcups 3.25.6
HP Deskjet 693, hpcups 3.25.6
HP Deskjet 694, hpcups 3.25.6
HP Deskjet 6940 Series, hpcups 3.25.6
HP Deskjet 695, hpcups 3.25.6
HP Deskjet 697, hpcups 3.25.6
HP Deskjet 6980 Series, hpcups 3.25.6
HP Deskjet 810c, hpcups 3.25.6
HP Deskjet 812c, hpcups 3.25.6
HP Deskjet 815c, hpcups 3.25.6
HP Deskjet 816c, hpcups 3.25.6
HP Deskjet 825c, hpcups 3.25.6
HP Deskjet 830c, hpcups 3.25.6
HP Deskjet 832c, hpcups 3.25.6
HP Deskjet 840c, hpcups 3.25.6
HP Deskjet 841c, hpcups 3.25.6
HP Deskjet 842c, hpcups 3.25.6
HP Deskjet 843c, hpcups 3.25.6
HP Deskjet 845c, hpcups 3.25.6
HP Deskjet 850c, hpcups 3.25.6
HP Deskjet 855c, hpcups 3.25.6
HP Deskjet 870c, hpcups 3.25.6
HP Deskjet 880c, hpcups 3.25.6
HP Deskjet 882c, hpcups 3.25.6
HP Deskjet 890c, hpcups 3.25.6
HP Deskjet 895c, hpcups 3.25.6
HP Deskjet 916c, hpcups 3.25.6
HP Deskjet 920c, hpcups 3.25.6
HP Deskjet 9300, hpcups 3.25.6
HP Deskjet 930c, hpcups 3.25.6
HP Deskjet 932c, hpcups 3.25.6
HP Deskjet 933c, hpcups 3.25.6
HP Deskjet 934c, hpcups 3.25.6
HP Deskjet 935c, hpcups 3.25.6
HP Deskjet 940c, hpcups 3.25.6
HP Deskjet 948c, hpcups 3.25.6
HP Deskjet 950c, hpcups 3.25.6
HP Deskjet 952c, hpcups 3.25.6
HP Deskjet 955c, hpcups 3.25.6
HP Deskjet 957c, hpcups 3.25.6
HP Deskjet 959c, hpcups 3.25.6
HP Deskjet 9600, hpcups 3.25.6
HP Deskjet 960c, hpcups 3.25.6
HP Deskjet 970c, hpcups 3.25.6
HP Deskjet 975c, hpcups 3.25.6
HP Deskjet 9800, hpcups 3.25.6
HP Deskjet 980c, hpcups 3.25.6
HP Deskjet 990c, hpcups 3.25.6
HP Deskjet 995c, hpcups 3.25.6
HP Deskjet Ink Adv 2010 k010, hpcups 3.25.6
HP Deskjet Ink Adv 2060 k110, hpcups 3.25.6
HP Deskjet Ink Advant k109a-z, hpcups 3.25.6
HP Deskjet Ink Advant k209a-z, hpcups 3.25.6
HP Deskjet Plus 4100 Series, hpcups 3.25.6
HP Deskjet Plus 6000 Series, hpcups 3.25.6
HP Deskjet Plus 6400 Series, hpcups 3.25.6
HP Deskjet d1300 Series, hpcups 3.25.6
HP Deskjet d1400 Series, hpcups 3.25.6
HP Deskjet d1500 Series, hpcups 3.25.6
HP Deskjet d1600 Series, hpcups 3.25.6
HP Deskjet d2300 Series, hpcups 3.25.6
HP Deskjet d2400 Series, hpcups 3.25.6
HP Deskjet d2500 Series, hpcups 3.25.6
HP Deskjet d2600 Series, hpcups 3.25.6
HP Deskjet d4100 Series, hpcups 3.25.6
HP Deskjet d4200 Series, hpcups 3.25.6
HP Deskjet d4300 Series, hpcups 3.25.6
HP Deskjet d5500 Series, hpcups 3.25.6
HP Deskjet d730, hpcups 3.25.6
HP Deskjet f2100 Series, hpcups 3.25.6
HP Deskjet f2200 Series, hpcups 3.25.6
HP Deskjet f2400 Series, hpcups 3.25.6
HP Deskjet f300 Series, hpcups 3.25.6
HP Deskjet f4100 Series, hpcups 3.25.6
HP Deskjet f4200 Series, hpcups 3.25.6
HP Deskjet f4400 Series, hpcups 3.25.6
HP Deskjet f4500 Series, hpcups 3.25.6
HP Deskjet f735, hpcups 3.25.6
HP Envy 100 d410 Series, hpcups 3.25.6
HP Envy 110 Series, hpcups 3.25.6
HP Envy 120 Series, hpcups 3.25.6
HP Envy 4500 Series, hpcups 3.25.6
HP Envy 4510 Series, hpcups 3.25.6
HP Envy 4520 Series, hpcups 3.25.6
HP Envy 5000 Series, hpcups 3.25.6
HP Envy 5530 Series, hpcups 3.25.6
HP Envy 5540 Series, hpcups 3.25.6
HP Envy 5640 Series, hpcups 3.25.6
HP Envy 5660 Series, hpcups 3.25.6
HP Envy 6000 Series, hpcups 3.25.6
HP Envy 6400 Series, hpcups 3.25.6
HP Envy 7640 Series, hpcups 3.25.6
HP Envy 8000 Series, hpcups 3.25.6
HP Envy Inspire 7200 Series, hpcups 3.25.6
HP Envy Inspire 7900 Series, hpcups 3.25.6
HP Envy Photo 6200 Series, hpcups 3.25.6
HP Envy Photo 7100 Series, hpcups 3.25.6
HP Envy Photo 7200 Series, hpcups 3.25.6
HP Envy Photo 7800 Series, hpcups 3.25.6
HP Envy Photo 7900 Series, hpcups 3.25.6
HP Envy Pro 6400 Series, hpcups 3.25.6
HP Ink Tank 110 Series, hpcups 3.25.6
HP Ink Tank 310 Series, hpcups 3.25.6
HP Ink Tank Wireless 410 Series, hpcups 3.25.6
HP LJ 300-400 color M351-M451 Postscript (recommended)
HP LJ 300-400 color MFP M375-M475 Postscript (recommended)
HP Laser Ns 1020, hpcups 3.25.6
HP Laser Ns MFP 1005, hpcups 3.25.6
HP LaserJet 100 color MFP M175 Postscript (recommended)
HP LaserJet 1000, hpcups 3.25.6, requires proprietary plugin
HP LaserJet 1005 Series, hpcups 3.25.6, requires proprietary plugin
HP LaserJet 1010, hpcups 3.25.6
HP LaserJet 1012, hpcups 3.25.6
HP LaserJet 1015, hpcups 3.25.6
HP LaserJet 1018, hpcups 3.25.6, requires proprietary plugin
HP LaserJet 1020, hpcups 3.25.6, requires proprietary plugin
HP LaserJet 1022 pcl3, hpcups 3.25.6, requires proprietary plugin
HP LaserJet 1022n pcl3, hpcups 3.25.6, requires proprietary plugin
HP LaserJet 1022nw pcl3, hpcups 3.25.6, requires proprietary plugin
HP LaserJet 1100, hpcups 3.25.6
HP LaserJet 1100a, hpcups 3.25.6
HP LaserJet 1100xi, hpcups 3.25.6
HP LaserJet 1150, hpcups 3.25.6
HP LaserJet 1160 Series, hpcups 3.25.6
HP LaserJet 1200 Postscript (recommended)
HP LaserJet 1200 pcl3, hpcups 3.25.6
HP LaserJet 1200n, hpcups 3.25.6
HP LaserJet 1220 Postscript (recommended)
HP LaserJet 1220 pcl3, hpcups 3.25.6
HP LaserJet 1220se, hpcups 3.25.6
HP LaserJet 1300 Series Postscript (recommended)
HP LaserJet 1300 pcl3, hpcups 3.25.6
HP LaserJet 1300n pcl3, hpcups 3.25.6
HP LaserJet 1300xi pcl3, hpcups 3.25.6
HP LaserJet 1320 Series pcl3, hpcups 3.25.6
HP LaserJet 1320 series Postscript (recommended)
HP LaserJet 1320, hpcups 3.25.6
HP LaserJet 1320n, hpcups 3.25.6
HP LaserJet 1320nw, hpcups 3.25.6
HP LaserJet 1320tn, hpcups 3.25.6
HP LaserJet 200 color M251 Postscript (recommended)
HP LaserJet 200 color MFP M275 Postscript (recommended)
HP LaserJet 200 color MFP M276 Postscript (recommended)
HP LaserJet 2100 Series Postscript (recommended)
HP LaserJet 2100 Series pcl3, hpcups 3.25.6
HP LaserJet 2200 Postscript (recommended)
HP LaserJet 2200 Series, hpcups 3.25.6
HP LaserJet 2300 Postscript (recommended)
HP LaserJet 2300 Series, hpcups 3.25.6
HP LaserJet 2410 Postscript (recommended)
HP LaserJet 2410 pcl3, hpcups 3.25.6
HP LaserJet 2420 Postscript (recommended)
HP LaserJet 2420 pcl3, hpcups 3.25.6
HP LaserJet 2430 Postscript (recommended)
HP LaserJet 2430 pcl3, hpcups 3.25.6
HP LaserJet 3015 Postscript (recommended)
HP LaserJet 3015 pcl3, hpcups 3.25.6
HP LaserJet 3020 3030 Postscript (recommended)
HP LaserJet 3020 pcl3, hpcups 3.25.6
HP LaserJet 3030 pcl3, hpcups 3.25.6
HP LaserJet 3050 Postscript (recommended)
HP LaserJet 3050 pcl3, hpcups 3.25.6
HP LaserJet 3052 Postscript (recommended)
HP LaserJet 3052 pcl3, hpcups 3.25.6
HP LaserJet 3055, hpcups 3.25.6
HP LaserJet 3100, hpcups 3.25.6
HP LaserJet 3150, hpcups 3.25.6
HP LaserJet 3200, hpcups 3.25.6
HP LaserJet 3200m Postscript (recommended)
HP LaserJet 3300 3310 3320 pcl3, hpcups 3.25.6
HP LaserJet 3300 Series Postscript (recommended)
HP LaserJet 3330, hpcups 3.25.6
HP LaserJet 3380 Postscript (recommended)
HP LaserJet 3380 pcl3, hpcups 3.25.6
HP LaserJet 3390 Postscript (recommended)
HP LaserJet 3390 pcl3, hpcups 3.25.6
HP LaserJet 3392, hpcups 3.25.6
HP LaserJet 4 Plus pcl3, hpcups 3.25.6
HP LaserJet 4 Plus v2013.111 Postscript (recommended)
HP LaserJet 4/4M PostScript 600DPI
HP LaserJet 400 M401 Postscript (recommended)
HP LaserJet 400 M401dne Postscript (recommended)
HP LaserJet 400 MFP M425 Postscript (recommended)
HP LaserJet 4000 Series Postscript (recommended)
HP LaserJet 4000 Series pcl3, hpcups 3.25.6
HP LaserJet 4050 Series Postscript (recommended)
HP LaserJet 4050 Series pcl3, hpcups 3.25.6
HP LaserJet 4100 MFP pcl3, hpcups 3.25.6
HP LaserJet 4100 MFP v.3010.107 Postscript (recommended)
HP LaserJet 4100 Series pcl3, hpcups 3.25.6
HP LaserJet 4100 Series v.3010.107 Postscript (recommended)
HP LaserJet 4150 Series, hpcups 3.25.6
HP LaserJet 4200 Series Postscript (recommended)
HP LaserJet 4200 pcl3, hpcups 3.25.6
HP LaserJet 4240 Postscript (recommended)
HP LaserJet 4240 pcl3, hpcups 3.25.6
HP LaserJet 4250 Postscript (recommended)
HP LaserJet 4250 pcl3, hpcups 3.25.6
HP LaserJet 4300 Series Postscript (recommended)
HP LaserJet 4300 pcl3, hpcups 3.25.6
HP LaserJet 4345 MFP Postscript (recommended)
HP LaserJet 4345 MFP pcl3, hpcups 3.25.6
HP LaserJet 4350 Postscript (recommended)
HP LaserJet 4350 pcl3, hpcups 3.25.6
HP LaserJet 4ML v2013.003 Postscript (recommended)
HP LaserJet 4MP v2013.103 Postscript (recommended)
HP LaserJet 4Si/4Si MX 600 dpi v2011.110 Postscript (recommended)
HP LaserJet 4l, hpcups 3.25.6
HP LaserJet 4ml, hpcups 3.25.6
HP LaserJet 4mp pcl3, hpcups 3.25.6
HP LaserJet 4si pcl3, hpcups 3.25.6
HP LaserJet 4v pcl3, hpcups 3.25.6
HP LaserJet 500 MFP M525 Postscript (recommended)
HP LaserJet 500 color M551 Postscript (recommended)
HP LaserJet 500 color MFP M570 Postscript (recommended)
HP LaserJet 500 color MFP M575 Postscript (recommended)
HP LaserJet 5000 Series Postscript (recommended)
HP LaserJet 5000 Series pcl3, hpcups 3.25.6
HP LaserJet 5100 Series Postscript (recommended)
HP LaserJet 5100 Series pcl3, hpcups 3.25.6
HP LaserJet 5200 Postscript (recommended)
HP LaserJet 5200 pcl3, hpcups 3.25.6
HP LaserJet 5200L Postscript (recommended)
HP LaserJet 5200LX Postscript (recommended)
HP LaserJet 5200l pcl3, hpcups 3.25.6
HP LaserJet 5200lx, hpcups 3.25.6
HP LaserJet 5MP Postscript (recommended)
HP LaserJet 5Si Mopier PS Postscript (recommended)
HP LaserJet 5l, hpcups 3.25.6
HP LaserJet 5mp pcl3, hpcups 3.25.6
HP LaserJet 5p, hpcups 3.25.6
HP LaserJet 5si Mopier pcl3, hpcups 3.25.6
HP LaserJet 5si pcl3, hpcups 3.25.6
HP LaserJet 600 M601 M602 M603 Postscript (recommended)
HP LaserJet 6P/6MP - PostScript
HP LaserJet 6l, hpcups 3.25.6
HP LaserJet 6mp pcl3, hpcups 3.25.6
HP LaserJet 6p, hpcups 3.25.6
HP LaserJet 700 M712 Postscript (recommended)
HP LaserJet 700 color MFP M775 Postscript (recommended)
HP LaserJet 8000 Series Postscript (recommended)
HP LaserJet 8000 Series pcl3, hpcups 3.25.6
HP LaserJet 8100 MFP, hpcups 3.25.6
HP LaserJet 8100 Series Postscript (recommended)
HP LaserJet 8100 Series pcl3, hpcups 3.25.6
HP LaserJet 8150 MFP, hpcups 3.25.6
HP LaserJet 8150 Series Postscript (recommended)
HP LaserJet 8150 Series pcl3, hpcups 3.25.6
HP LaserJet 8501 Postscript (recommended)
HP LaserJet 9000 MFP  Postscript (recommended)
HP LaserJet 9000 MFP pcl3, hpcups 3.25.6
HP LaserJet 9000 Series  Postscript (recommended)
HP LaserJet 9000 Series pcl3, hpcups 3.25.6
HP LaserJet 9040 9050 MFP Postscript (recommended)
HP LaserJet 9040 MFP pcl3, hpcups 3.25.6
HP LaserJet 9040 Postscript (recommended)
HP LaserJet 9040 pcl3, hpcups 3.25.6
HP LaserJet 9050 MFP pcl3, hpcups 3.25.6
HP LaserJet 9050 Postscript (recommended)
HP LaserJet 9050 pcl3, hpcups 3.25.6
HP LaserJet 9055 9065 MFP Postscript (recommended)
HP LaserJet 9055mfp pcl3, hpcups 3.25.6
HP LaserJet 9065mfp pcl3, hpcups 3.25.6
HP LaserJet CM1410 Series Postscript (recommended)
HP LaserJet CP1520 Series Postscript (recommended)
HP LaserJet E40040 Postscript (recommended)
HP LaserJet E50145 Postscript (recommended)
HP LaserJet E60055-E60075 Postscript (recommended)
HP LaserJet E60155 Postscript (recommended)
HP LaserJet E60165 Postscript (recommended)
HP LaserJet E60175 Postscript (recommended)
HP LaserJet E62555-E62575 Postscript (recommended)
HP LaserJet E62655-E62675 Postscript (recommended)
HP LaserJet Flow MFP E52645 Postscript (recommended)
HP LaserJet Flow MFP M528 Postscript (recommended)
HP LaserJet Flow MFP M630 Postscript (recommended)
HP LaserJet M1522 MFP Series Postscript (recommended)
HP LaserJet M1536dnf MFP Postscript (recommended)
HP LaserJet M2727 MFP Series Postscript (recommended)
HP LaserJet M3027 MFP Postscript (recommended)
HP LaserJet M3035 MFP Postscript (recommended)
HP LaserJet M406 Postscript (recommended)
HP LaserJet M407 Postscript (recommended)
HP LaserJet M4345 MFP Postscript (recommended)
HP LaserJet M4349 MFP Postscript (recommended)
HP LaserJet M4555 MFP Postscript (recommended)
HP LaserJet M5025 MFP Postscript (recommended)
HP LaserJet M5035 MFP Postscript (recommended)
HP LaserJet M506 Postscript (recommended)
HP LaserJet M507 Postscript (recommended)
HP LaserJet M607 M608 M609 Postscript (recommended)
HP LaserJet M610 M611 M612 Postscript (recommended)
HP LaserJet M806 Postscript (recommended)
HP LaserJet M9040 M9050 MFP Postscript (recommended)
HP LaserJet M9059  MFP Postscript (recommended)
HP LaserJet MFP 8601 Postscript (recommended)
HP LaserJet MFP E42540 Postscript (recommended)
HP LaserJet MFP E72425 Postscript (recommended)
HP LaserJet MFP E72430 Postscript (recommended)
HP LaserJet MFP E72525-30-35 Postscript (recommended)
HP LaserJet MFP E730 Postscript (recommended)
HP LaserJet MFP E73025 Postscript (recommended)
HP LaserJet MFP E73030 Postscript (recommended)
HP LaserJet MFP E731-30-35-40 Postscript (recommended)
HP LaserJet MFP E73130-35-40 Postscript (recommended)
HP LaserJet MFP E77822-25-30 Postscript (recommended)
HP LaserJet MFP E82540-50-60 Postscript (recommended)
HP LaserJet MFP E87640-50-60 Postscript (recommended)
HP LaserJet MFP M430 Postscript (recommended)
HP LaserJet MFP M431 Postscript (recommended)
HP LaserJet MFP M527 Postscript (recommended)
HP LaserJet MFP M630 Postscript (recommended)
HP LaserJet MFP M631 M632 M633 Postscript (recommended)
HP LaserJet MFP M634 M635 M636 Postscript (recommended)
HP LaserJet MFP M725 Postscript (recommended)
HP LaserJet MFP m129-m134, hpcups 3.25.6
HP LaserJet MFP m139-m142, hpcups 3.25.6
HP LaserJet MFP m232-m237, hpcups 3.25.6
HP LaserJet MFP m28-m31, hpcups 3.25.6
HP LaserJet Managed MFP E826-50-60-70 Postscript (recommended)
HP LaserJet Managed MFP E82650-60-70 Postscript (recommended)
HP LaserJet P2015 Series Postscript (recommended)
HP LaserJet P2055 Postscript (recommended)
HP LaserJet P3004 Postscript (recommended)
HP LaserJet P3005 Postscript (recommended)
HP LaserJet P3010 Series Postscript (recommended)
HP LaserJet P4010 Series Postscript (recommended)
HP LaserJet Pro 3001-3008 Postscript (recommended)
HP LaserJet Pro 4001 Postscript (recommended)
HP LaserJet Pro 4002 Postscript (recommended)
HP LaserJet Pro 4003 Postscript (recommended)
HP LaserJet Pro 4004 Postscript (recommended)
HP LaserJet Pro M118-M119 Postscript (recommended)
HP LaserJet Pro M148-M149 Postscript (recommended)
HP LaserJet Pro M148f-M149f Postscript (recommended)
HP LaserJet Pro M201-M202 Postscript (recommended)
HP LaserJet Pro M203-M206 Postscript (recommended)
HP LaserJet Pro M304-M305 Postscript (recommended)
HP LaserJet Pro M329 Postscript (recommended)
HP LaserJet Pro M402-M403 Postscript (recommended)
HP LaserJet Pro M402-M403n Postscript (recommended)
HP LaserJet Pro M404-M405 Postscript (recommended)
HP LaserJet Pro M428-M429 Postscript (recommended)
HP LaserJet Pro M428f-M429f Postscript (recommended)
HP LaserJet Pro M501 Postscript (recommended)
HP LaserJet Pro M701 Postscript (recommended)
HP LaserJet Pro M706 Postscript (recommended)
HP LaserJet Pro MFP 3101-3108 Postscript (recommended)
HP LaserJet Pro MFP 4101 Postscript (recommended)
HP LaserJet Pro MFP 4102 Postscript (recommended)
HP LaserJet Pro MFP 4103 Postscript (recommended)
HP LaserJet Pro MFP 4104 Postscript (recommended)
HP LaserJet Pro MFP M225-M226 Postscript (recommended)
HP LaserJet Pro MFP M227-M231 Postscript (recommended)
HP LaserJet Pro MFP M426-M427 Postscript (recommended)
HP LaserJet Pro MFP M435 Postscript (recommended)
HP LaserJet Pro MFP M521 Postscript (recommended)
HP LaserJet Pro MFP m125a, hpcups 3.25.6
HP LaserJet Pro MFP m125nr, hpcups 3.25.6
HP LaserJet Pro MFP m125nw, hpcups 3.25.6
HP LaserJet Pro MFP m125r, hpcups 3.25.6
HP LaserJet Pro MFP m125rnw, hpcups 3.25.6
HP LaserJet Pro MFP m125s, hpcups 3.25.6
HP LaserJet Pro MFP m126 Plus Series, hpcups 3.25.6
HP LaserJet Pro MFP m126a, hpcups 3.25.6
HP LaserJet Pro MFP m126nw, hpcups 3.25.6
HP LaserJet Pro MFP m127fn, hpcups 3.25.6
HP LaserJet Pro MFP m127fp, hpcups 3.25.6
HP LaserJet Pro MFP m127fs, hpcups 3.25.6
HP LaserJet Pro MFP m127fw, hpcups 3.25.6, requires proprietary plugin
HP LaserJet Pro MFP m128fn, hpcups 3.25.6
HP LaserJet Pro MFP m128fp, hpcups 3.25.6
HP LaserJet Pro MFP m128fw, hpcups 3.25.6
HP LaserJet Pro MFP m25a, hpcups 3.25.6
HP LaserJet Pro MFP m25nw, hpcups 3.25.6
HP LaserJet Pro MFP m26a, hpcups 3.25.6
HP LaserJet Pro MFP m26nw, hpcups 3.25.6
HP LaserJet Pro MFP m27c, hpcups 3.25.6
HP LaserJet Pro MFP m27cnw, hpcups 3.25.6
HP LaserJet Pro p1100 Plus Series, hpcups 3.25.6
HP LaserJet Professional m1132 MFP, hpcups 3.25.6
HP LaserJet Professional m1136 MFP, hpcups 3.25.6
HP LaserJet Professional m1137 MFP, hpcups 3.25.6
HP LaserJet Professional m1138 MFP, hpcups 3.25.6
HP LaserJet Professional m1139 MFP, hpcups 3.25.6
HP LaserJet Professional m1212nf MFP, hpcups 3.25.6
HP LaserJet Professional m1213nf MFP, hpcups 3.25.6
HP LaserJet Professional m1214nfh MFP, hpcups 3.25.6
HP LaserJet Professional m1216nfh MFP, hpcups 3.25.6
HP LaserJet Professional m1217nfw MFP, hpcups 3.25.6, requires proprietary plugin
HP LaserJet Professional m1218nfg MFP, hpcups 3.25.6
HP LaserJet Professional m1218nfs MFP, hpcups 3.25.6
HP LaserJet Professional m1219nf MFP, hpcups 3.25.6
HP LaserJet Professional m1219nfg MFP, hpcups 3.25.6
HP LaserJet Professional m1219nfs MFP, hpcups 3.25.6
HP LaserJet Professional p 1102w, hpcups 3.25.6
HP LaserJet Professional p1102, hpcups 3.25.6, requires proprietary plugin
HP LaserJet Professional p1106, hpcups 3.25.6
HP LaserJet Professional p1106w, hpcups 3.25.6
HP LaserJet Professional p1107, hpcups 3.25.6
HP LaserJet Professional p1107w, hpcups 3.25.6
HP LaserJet Professional p1108, hpcups 3.25.6
HP LaserJet Professional p1108w, hpcups 3.25.6
HP LaserJet Professional p1109, hpcups 3.25.6
HP LaserJet Professional p1109w, hpcups 3.25.6
HP LaserJet Professional p1566, hpcups 3.25.6, requires proprietary plugin
HP LaserJet Professional p1567, hpcups 3.25.6
HP LaserJet Professional p1568, hpcups 3.25.6
HP LaserJet Professional p1569, hpcups 3.25.6
HP LaserJet Professional p1606dn, hpcups 3.25.6
HP LaserJet Professional p1607dn, hpcups 3.25.6
HP LaserJet Professional p1608dn, hpcups 3.25.6
HP LaserJet Professional p1609dn, hpcups 3.25.6
HP LaserJet Tank 1020, hpcups 3.25.6
HP LaserJet Tank 150x, hpcups 3.25.6
HP LaserJet Tank 250x, hpcups 3.25.6
HP LaserJet Tank MFP 1005, hpcups 3.25.6
HP LaserJet Tank MFP 160x, hpcups 3.25.6
HP LaserJet Tank MFP 260x, hpcups 3.25.6
HP LaserJet cm1411fn pcl3, hpcups 3.25.6
HP LaserJet cm1412fn pcl3, hpcups 3.25.6
HP LaserJet cm1413fn pcl3, hpcups 3.25.6
HP LaserJet cm1415fn pcl3, hpcups 3.25.6
HP LaserJet cm1415fnw pcl3, hpcups 3.25.6
HP LaserJet cm1416fnw pcl3, hpcups 3.25.6
HP LaserJet cm1417fnw pcl3, hpcups 3.25.6
HP LaserJet cm1418fnw pcl3, hpcups 3.25.6
HP LaserJet color flow MFP M575 Postscript (recommended)
HP LaserJet cp1025, hpcups 3.25.6
HP LaserJet cp1025nw, hpcups 3.25.6, requires proprietary plugin
HP LaserJet flow MFP M525 Postscript (recommended)
HP LaserJet flow MFP M830 Postscript (recommended)
HP LaserJet m1005, hpcups 3.25.6, requires proprietary plugin
HP LaserJet m101-m106, hpcups 3.25.6
HP LaserJet m109-m112, hpcups 3.25.6
HP LaserJet m1120 MFP, hpcups 3.25.6, requires proprietary plugin
HP LaserJet m1120n MFP, hpcups 3.25.6, requires proprietary plugin
HP LaserJet m1319f MFP, hpcups 3.25.6, requires proprietary plugin
HP LaserJet m14-m17, hpcups 3.25.6
HP LaserJet m1522nf MFP pcl3, hpcups 3.25.6
HP LaserJet m1537dnf MFP pcl3, hpcups 3.25.6
HP LaserJet m1538dnf MFP pcl3, hpcups 3.25.6
HP LaserJet m1539dnf MFP pcl3, hpcups 3.25.6
HP LaserJet m207-m212, hpcups 3.25.6
HP LaserJet m2727 MFP pcl3, hpcups 3.25.6
HP LaserJet m3027 MFP pcl3, hpcups 3.25.6
HP LaserJet m3035 MFP pcl3, hpcups 3.25.6
HP LaserJet m4345 MFP pcl3, hpcups 3.25.6
HP LaserJet m4349 MFP pcl3, hpcups 3.25.6
HP LaserJet m5025 MFP pcl3, hpcups 3.25.6
HP LaserJet m5035 MFP pcl3, hpcups 3.25.6
HP LaserJet m5039 MFP pcl3, hpcups 3.25.6
HP LaserJet m9040 MFP pcl3, hpcups 3.25.6
HP LaserJet m9050 MFP pcl3, hpcups 3.25.6
HP LaserJet m9059 MFP pcl3, hpcups 3.25.6
HP LaserJet p1005, hpcups 3.25.6, requires proprietary plugin
HP LaserJet p1006, hpcups 3.25.6, requires proprietary plugin
HP LaserJet p1007, hpcups 3.25.6, requires proprietary plugin
HP LaserJet p1008, hpcups 3.25.6, requires proprietary plugin
HP LaserJet p1009, hpcups 3.25.6
HP LaserJet p1505, hpcups 3.25.6, requires proprietary plugin
HP LaserJet p1505n zxs, hpcups 3.25.6, requires proprietary plugin
HP LaserJet p2014 zxs, hpcups 3.25.6, requires proprietary plugin
HP LaserJet p2014n zxs, hpcups 3.25.6, requires proprietary plugin
HP LaserJet p2015 Series pcl3, hpcups 3.25.6
HP LaserJet p2015d Series, hpcups 3.25.6
HP LaserJet p2015dn Series, hpcups 3.25.6
HP LaserJet p2015n Series, hpcups 3.25.6
HP LaserJet p2015x Series, hpcups 3.25.6
HP LaserJet p2035 pcl3, hpcups 3.25.6, requires proprietary plugin
HP LaserJet p2035n pcl3, hpcups 3.25.6, requires proprietary plugin
HP LaserJet p2055 pcl3, hpcups 3.25.6
HP LaserJet p2055d pcl3, hpcups 3.25.6
HP LaserJet p2055dn pcl3, hpcups 3.25.6
HP LaserJet p2055x pcl3, hpcups 3.25.6
HP LaserJet p3004 pcl3, hpcups 3.25.6
HP LaserJet p3005 pcl3, hpcups 3.25.6
HP LaserJet p3010 Series pcl3, hpcups 3.25.6
HP LaserJet p4014, hpcups 3.25.6
HP LaserJet p4014dn, hpcups 3.25.6
HP LaserJet p4014n, hpcups 3.25.6
HP LaserJet p4015, hpcups 3.25.6
HP LaserJet p4015dn, hpcups 3.25.6
HP LaserJet p4015n, hpcups 3.25.6
HP LaserJet p4015tn, hpcups 3.25.6
HP LaserJet p4015x, hpcups 3.25.6
HP LaserJet p4515, hpcups 3.25.6
HP LaserJet p4515n, hpcups 3.25.6
HP LaserJet p4515tn, hpcups 3.25.6
HP LaserJet p4515x, hpcups 3.25.6
HP LaserJet p4515xm, hpcups 3.25.6
HP Laserjet M604 M605 M606 Postscript (recommended)
HP Mopier 240 Postscript (recommended)
HP Mopier 240 pcl3, hpcups 3.25.6
HP Mopier 320 Postscript (recommended)
HP Mopier 320 pcl3, hpcups 3.25.6
HP Neverstop Laser 100x, hpcups 3.25.6
HP Neverstop Laser MFP 120x, hpcups 3.25.6
HP OfficeJet Pro 8210 Postscript (recommended)
HP OfficeJet Pro 8730 Postscript (recommended)
HP OfficeJet Pro 8732M Postscript (recommended)
HP OfficeJet Pro 8740 Postscript (recommended)
HP Officejet 100 Mobile l411, hpcups 3.25.6
HP Officejet 150 Mobile l511, hpcups 3.25.6
HP Officejet 200 Mobile Series, hpcups 3.25.6
HP Officejet 250 Mobile Series, hpcups 3.25.6
HP Officejet 2620 Series, hpcups 3.25.6
HP Officejet 3830 Series, hpcups 3.25.6
HP Officejet 4000 k210, hpcups 3.25.6
HP Officejet 4100 Series, hpcups 3.25.6
HP Officejet 4105, hpcups 3.25.6
HP Officejet 4115 Series, hpcups 3.25.6
HP Officejet 4200 Series, hpcups 3.25.6
HP Officejet 4255, hpcups 3.25.6
HP Officejet 4300 Series, hpcups 3.25.6
HP Officejet 4400 k410, hpcups 3.25.6
HP Officejet 4500 g510a-f, hpcups 3.25.6
HP Officejet 4500 g510g-m, hpcups 3.25.6
HP Officejet 4500 g510n-z, hpcups 3.25.6
HP Officejet 4500 k710, hpcups 3.25.6
HP Officejet 4610 Series, hpcups 3.25.6
HP Officejet 4620 Series, hpcups 3.25.6
HP Officejet 4630 Series, hpcups 3.25.6
HP Officejet 4650 Series, hpcups 3.25.6
HP Officejet 5100 Series, hpcups 3.25.6
HP Officejet 5200 Series, hpcups 3.25.6
HP Officejet 5500 Series, hpcups 3.25.6
HP Officejet 5600 Series, hpcups 3.25.6
HP Officejet 5740 Series, hpcups 3.25.6
HP Officejet 6000 e609a, hpcups 3.25.6
HP Officejet 6000 e609n, hpcups 3.25.6
HP Officejet 6100 Series, hpcups 3.25.6
HP Officejet 6100, hpcups 3.25.6
HP Officejet 6150 Series, hpcups 3.25.6
HP Officejet 6200 Series, hpcups 3.25.6
HP Officejet 6300 Series, hpcups 3.25.6
HP Officejet 6500 e709a, hpcups 3.25.6
HP Officejet 6500 e709n, hpcups 3.25.6
HP Officejet 6500 e710a-f, hpcups 3.25.6
HP Officejet 6500 e710n-z, hpcups 3.25.6
HP Officejet 6600, hpcups 3.25.6
HP Officejet 6700, hpcups 3.25.6
HP Officejet 6800, hpcups 3.25.6
HP Officejet 6950, hpcups 3.25.6
HP Officejet 6960, hpcups 3.25.6
HP Officejet 7000 e809a Series, hpcups 3.25.6
HP Officejet 7100 Series, hpcups 3.25.6
HP Officejet 7110 Series, hpcups 3.25.6
HP Officejet 7200 Series, hpcups 3.25.6
HP Officejet 7300 Series, hpcups 3.25.6
HP Officejet 7400 Series, hpcups 3.25.6
HP Officejet 7500 e910, hpcups 3.25.6
HP Officejet 7510 Series, hpcups 3.25.6
HP Officejet 7610 Series, hpcups 3.25.6
HP Officejet 8010 Series, hpcups 3.25.6
HP Officejet 8020 Series, hpcups 3.25.6
HP Officejet 8040 Series, hpcups 3.25.6
HP Officejet 8120 Series, hpcups 3.25.6
HP Officejet 8120e Series, hpcups 3.25.6
HP Officejet 8130 Series, hpcups 3.25.6
HP Officejet 8130e Series, hpcups 3.25.6
HP Officejet 8700, hpcups 3.25.6
HP Officejet 9010 Series, hpcups 3.25.6
HP Officejet 9100 Series pcl3, hpcups 3.25.6
HP Officejet 9120 Series, hpcups 3.25.6
HP Officejet 9120e Series, hpcups 3.25.6
HP Officejet Color MFP X585 Postscript (recommended)
HP Officejet Color X555 Postscript (recommended)
HP Officejet D Series, hpcups 3.25.6
HP Officejet Lx, hpcups 3.25.6
HP Officejet Pro 1150c, hpcups 3.25.6
HP Officejet Pro 1170c Series, hpcups 3.25.6
HP Officejet Pro 251dw Printer Postscript (recommended)
HP Officejet Pro 276dw MFP Postscript (recommended)
HP Officejet Pro 3610, hpcups 3.25.6
HP Officejet Pro 3620, hpcups 3.25.6
HP Officejet Pro 6230, hpcups 3.25.6
HP Officejet Pro 6830, hpcups 3.25.6
HP Officejet Pro 6960, hpcups 3.25.6
HP Officejet Pro 6970, hpcups 3.25.6
HP Officejet Pro 7720 Series, hpcups 3.25.6
HP Officejet Pro 7730 Series, hpcups 3.25.6
HP Officejet Pro 7740 Series, hpcups 3.25.6
HP Officejet Pro 8000 Enterprise A811a Postscript (recommended)
HP Officejet Pro 8000 a809, hpcups 3.25.6
HP Officejet Pro 8020 Series, hpcups 3.25.6
HP Officejet Pro 8030 Series, hpcups 3.25.6
HP Officejet Pro 8100, hpcups 3.25.6
HP Officejet Pro 8120 Series, hpcups 3.25.6
HP Officejet Pro 8120e Series, hpcups 3.25.6
HP Officejet Pro 8130 Series, hpcups 3.25.6
HP Officejet Pro 8130e Series, hpcups 3.25.6
HP Officejet Pro 8500 a909a, hpcups 3.25.6
HP Officejet Pro 8500 a909g, hpcups 3.25.6
HP Officejet Pro 8500 a909n, hpcups 3.25.6
HP Officejet Pro 8500 a910, hpcups 3.25.6
HP Officejet Pro 8600, hpcups 3.25.6
HP Officejet Pro 8610, hpcups 3.25.6
HP Officejet Pro 8620, hpcups 3.25.6
HP Officejet Pro 8630, hpcups 3.25.6
HP Officejet Pro 8640, hpcups 3.25.6
HP Officejet Pro 8660, hpcups 3.25.6
HP Officejet Pro 8710, hpcups 3.25.6
HP Officejet Pro 8720, hpcups 3.25.6
HP Officejet Pro 9010 Series, hpcups 3.25.6
HP Officejet Pro 9020 Series, hpcups 3.25.6
HP Officejet Pro 9110 Series, hpcups 3.25.6
HP Officejet Pro 9110b Series, hpcups 3.25.6
HP Officejet Pro 9110e Series, hpcups 3.25.6
HP Officejet Pro 9120 Series, hpcups 3.25.6
HP Officejet Pro 9120b Series, hpcups 3.25.6
HP Officejet Pro 9120e Series, hpcups 3.25.6
HP Officejet Pro 9130 Series, hpcups 3.25.6
HP Officejet Pro 9130b Series, hpcups 3.25.6
HP Officejet Pro 9130e Series, hpcups 3.25.6
HP Officejet Pro 9720 Series, hpcups 3.25.6
HP Officejet Pro 9720e Series, hpcups 3.25.6
HP Officejet Pro 9730 Series, hpcups 3.25.6
HP Officejet Pro 9730e Series, hpcups 3.25.6
HP Officejet Pro X451-X551 Printer Postscript (recommended)
HP Officejet Pro X476-X576 MFP Postscript (recommended)
HP Officejet Pro k5300, hpcups 3.25.6
HP Officejet Pro k5400, hpcups 3.25.6
HP Officejet Pro k550, hpcups 3.25.6
HP Officejet Pro k850, hpcups 3.25.6
HP Officejet Pro k8600, hpcups 3.25.6
HP Officejet Pro l7300, hpcups 3.25.6
HP Officejet Pro l7400, hpcups 3.25.6
HP Officejet Pro l7500, hpcups 3.25.6
HP Officejet Pro l7600, hpcups 3.25.6
HP Officejet Pro l7700, hpcups 3.25.6
HP Officejet Series 300, hpcups 3.25.6
HP Officejet Series 310, hpcups 3.25.6
HP Officejet Series 320, hpcups 3.25.6
HP Officejet Series 330, hpcups 3.25.6
HP Officejet Series 350, hpcups 3.25.6
HP Officejet Series 520, hpcups 3.25.6
HP Officejet Series 570, hpcups 3.25.6
HP Officejet Series 580, hpcups 3.25.6
HP Officejet Series 590, hpcups 3.25.6
HP Officejet Series 600, hpcups 3.25.6
HP Officejet Series 610, hpcups 3.25.6
HP Officejet Series 630, hpcups 3.25.6
HP Officejet Series 700, hpcups 3.25.6
HP Officejet Series 710, hpcups 3.25.6
HP Officejet Series 720, hpcups 3.25.6
HP Officejet Series 725, hpcups 3.25.6
HP Officejet T Series, hpcups 3.25.6
HP Officejet g55, hpcups 3.25.6
HP Officejet g55xi, hpcups 3.25.6
HP Officejet g85, hpcups 3.25.6
HP Officejet g85xi, hpcups 3.25.6
HP Officejet g95, hpcups 3.25.6
HP Officejet h470, hpcups 3.25.6
HP Officejet j3500 Series, hpcups 3.25.6
HP Officejet j3600 Series, hpcups 3.25.6
HP Officejet j4500 Series, hpcups 3.25.6
HP Officejet j4660 Series, hpcups 3.25.6
HP Officejet j4680 Series, hpcups 3.25.6
HP Officejet j5500 Series, hpcups 3.25.6
HP Officejet j5700 Series, hpcups 3.25.6
HP Officejet j6400 Series, hpcups 3.25.6
HP Officejet k60, hpcups 3.25.6
HP Officejet k60xi, hpcups 3.25.6
HP Officejet k7100, hpcups 3.25.6
HP Officejet k80, hpcups 3.25.6
HP Officejet k80xi, hpcups 3.25.6
HP Officejet r40, hpcups 3.25.6
HP Officejet r40xi, hpcups 3.25.6
HP Officejet r45, hpcups 3.25.6
HP Officejet r60, hpcups 3.25.6
HP Officejet r65, hpcups 3.25.6
HP Officejet r80, hpcups 3.25.6
HP Officejet r80xi, hpcups 3.25.6
HP Officejet v30, hpcups 3.25.6
HP Officejet v40, hpcups 3.25.6
HP Officejet v40xi, hpcups 3.25.6
HP Officejet v45, hpcups 3.25.6
HP Officejet, hpcups 3.25.6
HP POSTSCRIPT INKJET DEVICES
HP POSTSCRIPT LASERJET DEVICES
HP POSTSCRIPT LASERJET PRO DEVICES
HP PSC 1000 Series, hpcups 3.25.6
HP PSC 1100 Series, hpcups 3.25.6
HP PSC 1200 Series, hpcups 3.25.6
HP PSC 1300 Series, hpcups 3.25.6
HP PSC 1310 Series, hpcups 3.25.6
HP PSC 1358 Series, hpcups 3.25.6
HP PSC 1400 Series, hpcups 3.25.6
HP PSC 1500 Series, hpcups 3.25.6
HP PSC 1600 Series, hpcups 3.25.6
HP PSC 2100 Series, hpcups 3.25.6
HP PSC 2150 Series, hpcups 3.25.6
HP PSC 2170 Series, hpcups 3.25.6
HP PSC 2200 Series, hpcups 3.25.6
HP PSC 2210 Series, hpcups 3.25.6
HP PSC 2300 Series, hpcups 3.25.6
HP PSC 2350 Series, hpcups 3.25.6
HP PSC 2400 Series, hpcups 3.25.6
HP PSC 2500 Series, hpcups 3.25.6
HP PSC 500, hpcups 3.25.6
HP PSC 720, hpcups 3.25.6
HP PSC 750, hpcups 3.25.6
HP PSC 750xi, hpcups 3.25.6
HP PSC 760, hpcups 3.25.6
HP PSC 780, hpcups 3.25.6
HP PSC 780xi, hpcups 3.25.6
HP PSC 900 Series, hpcups 3.25.6
HP PSC 920, hpcups 3.25.6
HP PSC 950, hpcups 3.25.6
HP PSC 950vr, hpcups 3.25.6
HP PSC 950xi, hpcups 3.25.6
HP PageWide Color 556 Postscript (recommended)
HP PageWide Color 755 Postscript (recommended)
HP PageWide Color E55650 Postscript (recommended)
HP PageWide Color E75160 Postscript (recommended)
HP PageWide Color E77650-E77660 Postscript (recommended)
HP PageWide Color Flow MFP 586 Postscript (recommended)
HP PageWide Color MFP 586 Postscript (recommended)
HP PageWide Color MFP 774 779 Postscript (recommended)
HP PageWide Color MFP 780-785 Postscript (recommended)
HP PageWide Color MFP E58650 Postscript (recommended)
HP PageWide Color P75250 Postscript (recommended)
HP PageWide MFP P57750 Postscript (recommended)
HP PageWide MFP P77740-60zs Postscript (recommended)
HP PageWide P55250 Postscript (recommended)
HP PageWide P75050-60 Postscript (recommended)
HP PageWide P77440 P77940-60 Postscript (recommended)
HP PageWide Pro 352 Printer Postscript (recommended)
HP PageWide Pro 377 MFP Postscript (recommended)
HP PageWide Pro 452 Printer Postscript (recommended)
HP PageWide Pro 477 MFP Postscript (recommended)
HP PageWide Pro 552 Printer Postscript (recommended)
HP PageWide Pro 577 MFP Postscript (recommended)
HP PageWide Pro 750 Postscript (recommended)
HP PageWide Pro MFP 772-777 Postscript (recommended)
HP PageWide XL 3900PS MFP PS3
HP PageWide XL 3920 PS MFP - PostScript
HP PageWide XL 4000 - PostScript
HP PageWide XL 4000 MFP - PostScript
HP PageWide XL 4100PS MFP PS3
HP PageWide XL 4100PS PS3
HP PageWide XL 4200 PS MFP series - PostScript
HP PageWide XL 4200 PS series - PostScript
HP PageWide XL 4500 - PostScript
HP PageWide XL 4500 MFP - PostScript
HP PageWide XL 4600PS MFP PS3
HP PageWide XL 4600PS PS3
HP PageWide XL 4700 PS MFP series - PostScript
HP PageWide XL 4700 PS series - PostScript
HP PageWide XL 5000 - PostScript
HP PageWide XL 5000 Blueprinter - PostScript
HP PageWide XL 5000 MFP - PostScript
HP PageWide XL 5100 - PostScript
HP PageWide XL 5100 MFP - PostScript
HP PageWide XL 5100 MFP Blueprinter - PostScript
HP PageWide XL 5200 PS MFP series - PostScript
HP PageWide XL 5200 PS series - PostScript
HP PageWide XL 6000 - PostScript
HP PageWide XL 6000 MFP - PostScript
HP PageWide XL 8000 - PostScript
HP PageWide XL 8000 Blueprinter - PostScript
HP PageWide XL 8200 PS series - PostScript
HP PageWide XL Pro 5200 PS MFP series - PostScript
HP PageWide XL Pro 8200 PS MFP series - PostScript
HP Photosmart 100, hpcups 3.25.6
HP Photosmart 1115, hpcups 3.25.6
HP Photosmart 1215, hpcups 3.25.6
HP Photosmart 1218, hpcups 3.25.6
HP Photosmart 130, hpcups 3.25.6
HP Photosmart 1315, hpcups 3.25.6
HP Photosmart 140 Series, hpcups 3.25.6
HP Photosmart 230, hpcups 3.25.6
HP Photosmart 240 Series, hpcups 3.25.6
HP Photosmart 2570 Series, hpcups 3.25.6
HP Photosmart 2600 Series, hpcups 3.25.6
HP Photosmart 2700 Series, hpcups 3.25.6
HP Photosmart 3100 Series, hpcups 3.25.6
HP Photosmart 320 Series, hpcups 3.25.6
HP Photosmart 3200 Series, hpcups 3.25.6
HP Photosmart 330 Series, hpcups 3.25.6
HP Photosmart 3300 Series, hpcups 3.25.6
HP Photosmart 370 Series, hpcups 3.25.6
HP Photosmart 380 Series, hpcups 3.25.6
HP Photosmart 420 Series, hpcups 3.25.6
HP Photosmart 470 Series, hpcups 3.25.6
HP Photosmart 5510 Series, hpcups 3.25.6
HP Photosmart 5510d Series, hpcups 3.25.6
HP Photosmart 5520 Series, hpcups 3.25.6
HP Photosmart 6510 Series, hpcups 3.25.6
HP Photosmart 6520 Series, hpcups 3.25.6
HP Photosmart 7200 Series, hpcups 3.25.6
HP Photosmart 7345, hpcups 3.25.6
HP Photosmart 7400 Series, hpcups 3.25.6
HP Photosmart 7510 Series, hpcups 3.25.6
HP Photosmart 7520 Series, hpcups 3.25.6
HP Photosmart 7550, hpcups 3.25.6
HP Photosmart 7600 Series, hpcups 3.25.6
HP Photosmart 7700 Series, hpcups 3.25.6
HP Photosmart 7800 Series, hpcups 3.25.6
HP Photosmart 7900 Series, hpcups 3.25.6
HP Photosmart 8000 Series, hpcups 3.25.6
HP Photosmart 8100 Series, hpcups 3.25.6
HP Photosmart 8200 Series, hpcups 3.25.6
HP Photosmart 8400 Series, hpcups 3.25.6
HP Photosmart 8700 Series, hpcups 3.25.6
HP Photosmart Estn c510 Series, hpcups 3.25.6
HP Photosmart Ink Adv k510, hpcups 3.25.6
HP Photosmart Plus b209a-m, hpcups 3.25.6
HP Photosmart Plus b210 Series, hpcups 3.25.6
HP Photosmart Prem c310 Series, hpcups 3.25.6
HP Photosmart Prem c410 Series, hpcups 3.25.6
HP Photosmart Prem-web c309n-s, hpcups 3.25.6
HP Photosmart Premium c309g-m, hpcups 3.25.6
HP Photosmart Pro b8300 Series, hpcups 3.25.6
HP Photosmart Pro b8800 Series, hpcups 3.25.6
HP Photosmart Wireless b109n-z, hpcups 3.25.6
HP Photosmart a310 Series, hpcups 3.25.6
HP Photosmart a320 Series, hpcups 3.25.6
HP Photosmart a430 Series, hpcups 3.25.6
HP Photosmart a440 Series, hpcups 3.25.6
HP Photosmart a510 Series, hpcups 3.25.6
HP Photosmart a520 Series, hpcups 3.25.6
HP Photosmart a530 Series, hpcups 3.25.6
HP Photosmart a610 Series, hpcups 3.25.6
HP Photosmart a620 Series, hpcups 3.25.6
HP Photosmart a630 Series, hpcups 3.25.6
HP Photosmart a640 Series, hpcups 3.25.6
HP Photosmart a710 Series, hpcups 3.25.6
HP Photosmart a820 Series, hpcups 3.25.6
HP Photosmart b010 Series, hpcups 3.25.6
HP Photosmart b109a Series, hpcups 3.25.6
HP Photosmart b110 Series, hpcups 3.25.6
HP Photosmart b8500 Series, hpcups 3.25.6
HP Photosmart c309a Series, hpcups 3.25.6
HP Photosmart c3100 Series, hpcups 3.25.6
HP Photosmart c4100 Series, hpcups 3.25.6
HP Photosmart c4200 Series, hpcups 3.25.6
HP Photosmart c4340 Series, hpcups 3.25.6
HP Photosmart c4380 Series, hpcups 3.25.6
HP Photosmart c4400 Series, hpcups 3.25.6
HP Photosmart c4500 Series, hpcups 3.25.6
HP Photosmart c4600 Series, hpcups 3.25.6
HP Photosmart c4700 Series, hpcups 3.25.6
HP Photosmart c5100 Series, hpcups 3.25.6
HP Photosmart c5200 Series, hpcups 3.25.6
HP Photosmart c5300 Series, hpcups 3.25.6
HP Photosmart c5500 Series, hpcups 3.25.6
HP Photosmart c6100 Series, hpcups 3.25.6
HP Photosmart c6200 Series, hpcups 3.25.6
HP Photosmart c6300 Series, hpcups 3.25.6
HP Photosmart c7100 Series, hpcups 3.25.6
HP Photosmart c7200 Series, hpcups 3.25.6
HP Photosmart c8100 Series, hpcups 3.25.6
HP Photosmart d110 Series, hpcups 3.25.6
HP Photosmart d5060 Series, hpcups 3.25.6
HP Photosmart d5100 Series, hpcups 3.25.6
HP Photosmart d5300 Series, hpcups 3.25.6
HP Photosmart d5400 Series, hpcups 3.25.6
HP Photosmart d6100 Series, hpcups 3.25.6
HP Photosmart d7100 Series, hpcups 3.25.6
HP Photosmart d7200 Series, hpcups 3.25.6
HP Photosmart d7300 Series, hpcups 3.25.6
HP Photosmart d7400 Series, hpcups 3.25.6
HP Photosmart d7500 Series, hpcups 3.25.6
HP Photosmart p1000, hpcups 3.25.6
HP Photosmart p1100, hpcups 3.25.6
HP Printer Scanner Copier 300, hpcups 3.25.6
HP Smart Tank 210-220 Series, hpcups 3.25.6
HP Smart Tank 350 Series, hpcups 3.25.6
HP Smart Tank 500 Series, hpcups 3.25.6
HP Smart Tank 510 Series, hpcups 3.25.6
HP Smart Tank 5100 Series, hpcups 3.25.6
HP Smart Tank 520 540 Series, hpcups 3.25.6
HP Smart Tank 530 Series, hpcups 3.25.6
HP Smart Tank 580-590 Series, hpcups 3.25.6
HP Smart Tank 6000 Series, hpcups 3.25.6
HP Smart Tank 610 Series, hpcups 3.25.6
HP Smart Tank 660-670 Series, hpcups 3.25.6
HP Smart Tank 7000 Series, hpcups 3.25.6
HP Smart Tank 710-720 Series, hpcups 3.25.6
HP Smart Tank 7300 Series, hpcups 3.25.6
HP Smart Tank 750 Series, hpcups 3.25.6
HP Smart Tank 7600 Series, hpcups 3.25.6
HP Smart Tank 790 Series, hpcups 3.25.6
HP Smart Tank Plus 550 Series, hpcups 3.25.6
HP Smart Tank Plus 570 Series, hpcups 3.25.6
HP Smart Tank Plus 650 Series, hpcups 3.25.6
HP Smart Tank Wireless 450 Series, hpcups 3.25.6
HP Tango, hpcups 3.25.6
HP cp1160, hpcups 3.25.6
hplip-ppds *NickName:		"HP LaserJet 5Si/5Si MX PostScript
hplip-ppds *NickName:  	"HP LaserJet 4V/4MV PostScript

## foo2zjs — 101 个型号

Dell 1355 Foomatic/foo2hbpl2 (recommended)
Dell C1765 Foomatic/foo2hbpl2 (recommended)
Epson AcuLaser CX17NF Foomatic/foo2hbpl2 (recommended)
Epson AcuLaser M1400 Foomatic/foo2hbpl2 (recommended)
Fuji Xerox DocuPrint CM205 Foomatic/foo2hbpl2 (recommended)
Fuji Xerox DocuPrint CM215 Foomatic/foo2hbpl2 (recommended)
Fuji Xerox DocuPrint M215 Foomatic/foo2hbpl2 (recommended)
Fuji Xerox DocuPrint P205 Foomatic/foo2hbpl2 (recommended)
Generic DDST Printer Foomatic/foo2ddst
Generic GDI Printer Foomatic/foo2zjs
Generic OAKT Printer Foomatic/foo2oak (recommended)
Generic ZJS Foomatic/foo2hp
Generic ZjStream Printer Foomatic/foo2zjs (recommended)
HP Color LaserJet 1500 Foomatic/foo2oak (recommended)
HP Color LaserJet 1600 Foomatic/foo2hp (recommended)
HP Color LaserJet 2600n Foomatic/foo2hp (recommended)
HP Color LaserJet CP1215 Foomatic/foo2hp (recommended)
HP LaserJet 1000 Foomatic/foo2zjs (recommended)
HP LaserJet 1005 Foomatic/foo2zjs (recommended)
HP LaserJet 1018 Foomatic/foo2zjs-z1 (recommended)
HP LaserJet 1020 Foomatic/foo2zjs-z1 (recommended)
HP LaserJet 1022 Foomatic/foo2zjs-z1 (recommended)
HP LaserJet 1022n Foomatic/foo2zjs-z1 (recommended)
HP LaserJet 1022nw Foomatic/foo2zjs-z1 (recommended)
HP LaserJet M1005 MFP Foomatic/foo2xqx (recommended)
HP LaserJet M1120 MFP Foomatic/foo2xqx (recommended)
HP LaserJet M1319 MFP Foomatic/foo2zjs-z1 (recommended)
HP LaserJet P1005 Foomatic/foo2xqx (recommended)
HP LaserJet P1006 Foomatic/foo2xqx (recommended)
HP LaserJet P1007 Foomatic/foo2xqx (recommended)
HP LaserJet P1008 Foomatic/foo2xqx (recommended)
HP LaserJet P1505 Foomatic/foo2xqx (recommended)
HP LaserJet P1505n Foomatic/foo2xqx (recommended)
HP LaserJet P2014 Foomatic/foo2xqx (recommended)
HP LaserJet P2014n Foomatic/foo2xqx (recommended)
HP LaserJet P2035 Foomatic/foo2zjs-z1 (recommended)
HP LaserJet P2035n Foomatic/foo2zjs-z1 (recommended)
HP LaserJet Pro CP1025nw Foomatic/foo2zjs-z3 (recommended)
HP LaserJet Pro M1132s MFP Foomatic/foo2xqx (recommended)
HP LaserJet Pro M12a Foomatic/foo2zjs-z2 (recommended)
HP LaserJet Pro M12w Foomatic/foo2zjs-z2 (recommended)
HP LaserJet Pro P1102 Foomatic/foo2zjs-z2 (recommended)
HP LaserJet Pro P1102w Foomatic/foo2zjs-z2 (recommended)
HP LaserJet Pro P1566 Foomatic/foo2zjs-z2 (recommended)
HP LaserJet Pro P1606dn Foomatic/foo2zjs-z2 (recommended)
HP LaserJet Professional M1212nf MFP Foomatic/foo2xqx (recommended)
KONICA MINOLTA magicolor 1600W Foomatic/foo2lava (recommended)
KONICA MINOLTA magicolor 1680MF Foomatic/foo2lava (recommended)
KONICA MINOLTA magicolor 1690MF Foomatic/foo2lava (recommended)
KONICA MINOLTA magicolor 2430 DL Foomatic/foo2zjs (recommended)
KONICA MINOLTA magicolor 2480 MF Foomatic/foo2lava (recommended)
KONICA MINOLTA magicolor 2490 MF Foomatic/foo2lava (recommended)
KONICA MINOLTA magicolor 2530 DL Foomatic/foo2lava (recommended)
KONICA MINOLTA magicolor 4690MF Foomatic/foo2lava (recommended)
Kyocera KM-1635 Foomatic/foo2oak-z1 (recommended)
Kyocera KM-2035 Foomatic/foo2oak-z1 (recommended)
Lexmark C500 Foomatic/foo2slx (recommended)
Minolta Color PageWorks/Pro L Foomatic/foo2zjs (recommended)
Minolta magicolor 2200 DL Foomatic/foo2zjs (recommended)
Minolta magicolor 2300 DL Foomatic/foo2zjs (recommended)
Minolta magicolor 2430 DL Foomatic/foo2zjs (recommended)
Oki C110 Foomatic/foo2lava (recommended)
Oki C301dn Foomatic/foo2hiperc (recommended)
Oki C3100 Foomatic/foo2hiperc (recommended)
Oki C310dn Foomatic/foo2hiperc (recommended)
Oki C3200 Foomatic/foo2hiperc (recommended)
Oki C3300 Foomatic/foo2hiperc (recommended)
Oki C3400 Foomatic/foo2hiperc (recommended)
Oki C3530 MFP Foomatic/foo2hiperc (recommended)
Oki C5100 Foomatic/foo2hiperc (recommended)
Oki C511dn Foomatic/foo2hiperc (recommended)
Oki C5200 Foomatic/foo2hiperc (recommended)
Oki C5500 Foomatic/foo2hiperc (recommended)
Oki C5600 Foomatic/foo2hiperc (recommended)
Oki C5650 Foomatic/foo2hiperc (recommended)
Oki C5800 Foomatic/foo2hiperc (recommended)
Oki C810 Foomatic/foo2hiperc-z1 (recommended)
Olivetti d-Color P160W Foomatic/foo2hiperc (recommended)
Ricoh SP 112 Foomatic/foo2ddst (recommended)
Ricoh SP 201Nw Foomatic/foo2ddst (recommended)
Samsung CLP-300 Foomatic/foo2qpdl (recommended)
Samsung CLP-310 Foomatic/foo2qpdl (recommended)
Samsung CLP-315 Foomatic/foo2qpdl (recommended)
Samsung CLP-325 Foomatic/foo2qpdl (recommended)
Samsung CLP-365 Foomatic/foo2qpdl (recommended)
Samsung CLP-600 Foomatic/foo2qpdl (recommended)
Samsung CLP-610 Foomatic/foo2qpdl (recommended)
Samsung CLP-620 Foomatic/foo2qpdl (recommended)
Samsung CLX-2160 Foomatic/foo2qpdl (recommended)
Samsung CLX-3160 Foomatic/foo2qpdl (recommended)
Samsung CLX-3175 Foomatic/foo2qpdl (recommended)
Samsung CLX-3185 Foomatic/foo2qpdl (recommended)
Samsung ML-1670 Foomatic/foo2qpdl (recommended)
Samsung ML-1675 Foomatic/foo2qpdl (recommended)
Xerox Phaser 3010 Foomatic/foo2hbpl2 (recommended)
Xerox Phaser 3040 Foomatic/foo2hbpl2 (recommended)
Xerox Phaser 6110 Foomatic/foo2qpdl (recommended)
Xerox Phaser 6115MFP Foomatic/foo2lava (recommended)
Xerox Phaser 6121MFP Foomatic/foo2lava (recommended)
Xerox WorkCentre 3045 Foomatic/foo2hbpl2 (recommended)
Xerox WorkCentre 6015 Foomatic/foo2hbpl2 (recommended)

## splix — 86 个型号

Dell 1100, 2.0.0
Dell 1110, 2.0.0
Lexmark X215 MFP, 2.0.0
Samsung CLP-200, 2.0.0
Samsung CLP-300, 2.0.0
Samsung CLP-310, 2.0.0
Samsung CLP-310N, 2.0.0
Samsung CLP-315, 2.0.0
Samsung CLP-500, 2.0.0
Samsung CLP-510, 2.0.0
Samsung CLP-550, 2.0.0
Samsung CLP-600, 2.0.0
Samsung CLX-216X, 2.0.0
Samsung CLX-2170, 2.0.0
Samsung CLX-3160, 2.0.0
Samsung ML-1510, 2.0.0
Samsung ML-1520, 2.0.0
Samsung ML-1610, 2.0.0
Samsung ML-1630, 2.0.0
Samsung ML-1640, 2.0.0
Samsung ML-1660, 2.0.0
Samsung ML-1710, 2.0.0
Samsung ML-1740, 2.0.0
Samsung ML-1750, 2.0.0
Samsung ML-1910, 2.0.0
Samsung ML-1915, 2.0.0
Samsung ML-2010, 2.0.0
Samsung ML-2015, 2.0.0
Samsung ML-2150, 2.0.0
Samsung ML-2160, 2.0.0
Samsung ML-2165, 2.0.0
Samsung ML-2240, 2.0.0
Samsung ML-2250, 2.0.0
Samsung ML-2251, 2.0.0
Samsung ML-2510, 2.0.0
Samsung ML-2525, 2.0.0
Samsung ML-2525W, 2.0.0
Samsung ML-2550, 2.0.0
Samsung ML-2571, 2.0.0
Samsung ML-2580, 2.0.0
Samsung ML-2580N, 2.0.0
Samsung ML-3050, 2.0.0
Samsung ML-3051, 2.0.0
Samsung ML-3051ND, 2.0.0
Samsung ML-3310, 2.0.0
Samsung ML-3310ND, 2.0.0
Samsung ML-3471ND, 2.0.0
Samsung ML-3560, 2.0.0
Samsung SCX-3200, 2.0.0
Samsung SCX-4100, 2.0.0
Samsung SCX-4200, 2.0.0
Samsung SCX-4216F, 2.0.0
Samsung SCX-4300, 2.0.0
Samsung SCX-4500, 2.0.0
Samsung SCX-4521F, 2.0.0
Samsung SCX-4600, 2.0.0
Samsung SCX-4623f, 2.0.0
Samsung SCX-4623fw, 2.0.0
Samsung SCX-5330N, 2.0.0
Samsung SCX-5530FN, 2.0.0
Samsung SF-565P, 2.0.0
Samsung TRANSLATE ML-2160, 2.0.0
Samsung TRANSLATE ML-2165, 2.0.0
Samsung TRANSLATE ML-3310, 2.0.0
Samsung TRANSLATE ML-3310ND, 2.0.0
Toshiba eSTUDIO180S, 2.0.0
Xerox Phaser 3115, 2.0.0
Xerox Phaser 3116, 2.0.0
Xerox Phaser 3117, 2.0.0
Xerox Phaser 3120, 2.0.0
Xerox Phaser 3121, 2.0.0
Xerox Phaser 3122, 2.0.0
Xerox Phaser 3124, 2.0.0
Xerox Phaser 3130, 2.0.0
Xerox Phaser 3140, 2.0.0
Xerox Phaser 3150, 2.0.0
Xerox Phaser 3155, 2.0.0
Xerox Phaser 3160, 2.0.0
Xerox Phaser 3420, 2.0.0
Xerox Phaser 3425, 2.0.0
Xerox Phaser 5500, 2.0.0
Xerox Phaser 6100, 2.0.0
Xerox Phaser 6110, 2.0.0
Xerox WorkCentre 3119, 2.0.0
Xerox WorkCentre PE114e, 2.0.0
Xerox WorkCentre PE16, 2.0.0

## brlaser — 29 个型号（drv）

DCP-1510
DCP-1600 series
DCP-7030
DCP-7040
DCP-7055
DCP-7055W
DCP-7060D
DCP-7065DN
DCP-7080
DCP-7080D
DCP-L2500D
DCP-L2520D
DCP-L2540DW
HL-1110
HL-1200
HL-2030 series
HL-2140 series
HL-2220 series
HL-2270DW series
HL-5030 series
HL-L2300D
HL-L2320D
HL-L2340D
HL-L2360D
MFC-1910W
MFC-7240
MFC-7360N
MFC-7365DN
MFC-L2710DW series

## brhl3040cn — 1 个型号

Brother HL-3040CN / HL-3070CW（彩色 LED，与 3070CW 同代引擎）：闭源 i386 filter，需 box86 转译运行
