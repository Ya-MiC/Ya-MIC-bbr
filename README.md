# Ya-MIC - BBR 网络加速管理脚本
# All project source codes are not open yet but projects can be used

![GitHub](https://img.shields.io/badge/License-MIT-blue.svg)  
![BBR](https://img.shields.io/badge/BBR-Optimized-green.svg)  

**Ya-MIC** 是一个基于 **byJoey 思路** 优化的 BBR（Bottleneck Bandwidth and Round-trip）管理脚本，旨在提供更高效的 TCP 拥塞控制，优化网络传输性能，降低延迟并提升带宽利用率。


---

## 📌 功能特性
✅ **一键安装 & 管理 BBR**（支持 BBRv2/v3 及自定义优化参数）  
✅ **智能动态调整**（基于 AIMD 策略改进，增强公平性和响应速度）  
✅ **多平台支持**（适配主流 Linux 发行版：Debian/Ubuntu/CentOS 等）  
✅ **低开销 & 高性能**（优化内核参数，减少资源占用）  
✅ **未来扩展性**（持续更新，计划支持 QUIC 和更灵敏的 RTT 探测）  

---

## 🚀 快速开始

### 安装方式
```bash
wget https://github.com/Ya-MIC/bbr-manager/raw/main/install.sh
chmod +x install.sh
sudo ./install.sh
```

### 配置选项
运行脚本后，可选择以下模式：
- **标准 BBR**（默认优化参数）  
- **激进模式**（更高带宽利用率，适合低丢包网络）  
- **兼容模式**（平衡延迟和吞吐量）  

### 卸载脚本
```bash
sudo ./install.sh --uninstall
```

---

## 📚 技术背景
本脚本基于 **byJoey 的 BBR 优化思路**，主要改进包括：
- **动态 AIMD 混合策略**：在 BBR 基础上引入更平滑的速率调整，减少突发流量影响。  
- **RTT 自适应探测**：优化探测间隔，避免过度占用带宽。  
- **多队列支持**：适配现代多核服务器，减少锁竞争。  

---

## 🔮 未来计划
- [ ] **BBRv3 深度适配**（测试最新 Linux 内核的 BBR 改进）  
- [ ] **QUIC/HTTP3 支持**（扩展至 UDP 传输层优化）  
- [ ] **可视化监控面板**（实时查看带宽、延迟等指标）  

---

## 📜 许可证
MIT License | Copyright © 2024 Ya-MIC  

---

## 🤝 贡献与反馈
欢迎提交 Issue 或 PR！  
📧 联系作者：`cao417090217@gmail.com`  

---

### 备注
- 请根据实际脚本功能调整参数和描述。  




BBR 管理脚本
这是一个功能强大又超可爱的脚本，用于管理Linux下的BBR拥有塞控制算法和队列管理算法。无论是安装BBR v3，还是切换到更适合您的加速方式，这里统统搞定！
主要支持Ubuntu系统

🌟功能列表
👑一键安装 BBR v3 内核
🍰切换加速模式（BBR+FQ、BBR+CAKE 等）
⚙️开启/关闭 BBR
🗑️卸载加速内核，告别不需要的内核版本
👀实时查看当前 TCP 拥塞算法和队列算法
🎨美化的输出界面，让剧本灵魂更多

byJoey思路：

一键运行脚本
```bash
<(curl -l -s https://raw.githubusercontent.com/byJoey/Actions-bbr-v3/refs/heads/main/install.sh)

```



操作界面
╭( ･ㅂ･)و ✧ 你可以选择以下操作哦：
  1. 🛠️  安装 BBR v3
  2. 🔍 检查是否为 BBR v3
  3. ⚡ 使用 BBR + FQ 加速
  4. ⚡ 使用 BBR + FQ_PIE 加速
  5. ⚡ 使用 BBR + CAKE 加速
  6. 🔧 开启或关闭 BBR
  7. 🗑️  卸载


一切以脚本内部数据为准

BBR + FQ 是最常见的方案，适用于大多数场景

记得备份你的内核
免责声明：任何使用问题请自负风险！

🌟特别鸣谢
感谢Naochen2799/Latest-Kernel-BBR3项目提供的技术支持和灵感参考。








