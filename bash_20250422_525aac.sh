#!/bin/bash
# 用于启用BBR的脚本（需要root权限）
echo "Enabling BBR..."
echo "net.core.default_qdisc=fq" >> /etc/sysctl.conf
echo "net.ipv4.tcp_congestion_control=bbr" >> /etc/sysctl.conf
sysctl -p
sysctl net.ipv4.tcp_congestion_control
echo "BBR enabled successfully!"
