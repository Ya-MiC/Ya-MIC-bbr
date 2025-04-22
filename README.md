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

一键运行脚本
bash <(curl -l -s https://raw.githubusercontent.com/byJoey/Actions-bbr-v3/refs/heads/main/install.sh)

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

感谢joey提供思路希望获得vps对我的未来的个人项目进行修改和创建







