Raspberry Pi 4

iotadmin@iot-pi:~ $ ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
    link/ether dc:a6:32:de:73:94 brd ff:ff:ff:ff:ff:ff
    inet 150.201.166.11/23 brd 150.201.167.255 scope global dynamic noprefixroute eth0
       valid_lft 75sec preferred_lft 75sec
    inet6 fe80::dea6:32ff:fede:7394/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
3: wlan0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN group default qlen 1000
    link/ether dc:a6:32:de:73:95 brd ff:ff:ff:ff:ff:ff

iotadmin@iot-pi:~ $ hostname
iot-pi

Workstation

PS C:\Users\tachowdhury> ipconfig
Windows IP Configuration
Ethernet adapter Ethernet:

   Connection-specific DNS Suffix  . : semo.edu
   Link-local IPv6 Address . . . . . : fe80::8c7c:3a70:e9f3:b998%9
   IPv4 Address. . . . . . . . . . . : 150.201.167.242
   Subnet Mask . . . . . . . . . . . : 255.255.254.0
   Default Gateway . . . . . . . . . : 150.201.167.254

Device name	A-1909010004
Full device name	A-1909010004.semo.edu
Processor	Intel(R) Core(TM) i3-8100 CPU @ 3.60GHz (3.60 GHz)
Installed RAM	16.0 GB (15.9 GB usable)
Device ID	4C418AAB-BEA7-4F61-9B9B-7181C8A662BB
Product ID	00328-10000-00001-AA220
System type	64-bit operating system, x64-based processor
Pen and touch	No pen or touch input is available for this display

MacBook Pro 2020

ctarique@Tariques-MacBook-Pro ~ % ifconfig

en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
	options=6460<TSO4,TSO6,CHANNEL_IO,PARTIAL_CSUM,ZEROINVERT_CSUM>
	ether a0:78:17:7c:3c:1c
	inet6 fe80::1c62:9005:2f78:6d64%en0 prefixlen 64 secured scopeid 0xb 
	inet 150.201.168.242 netmask 0xfffffc00 broadcast 150.201.171.255
	nd6 options=201<PERFORMNUD,DAD>
	media: autoselect
	status: active

ESP32

Chip type:          ESP32-D0WDQ6 (revision v1.0)
Features:           Wi-Fi, BT, Dual Core + LP Core, 240MHz, Vref calibration in eFuse, Coding Scheme None
Crystal frequency:  40MHz
MAC:                94:b9:7e:e4:3f:0c
