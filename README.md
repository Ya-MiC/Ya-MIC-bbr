

# **BBR (Bottleneck Bandwidth and Round-trip) Optimization Guide**  
*A high-performance TCP congestion control algorithm for Linux*  

![BBR Logo](https://img.shields.io/badge/BBR-Optimized-green)  
![Linux](https://img.shields.io/badge/OS-Linux-blue)  
![License](https://img.shields.io/badge/License-MIT-orange)  

---

## **📌 What is BBR?**  
BBR (**Bottleneck Bandwidth and Round-trip propagation time**) is a **TCP congestion control algorithm** developed by Google. Unlike traditional loss-based algorithms (e.g., CUBIC), BBR:  
✅ **Dynamically adjusts sending rates** based on real-time bandwidth and latency.  
✅ **Reduces bufferbloat** (excessive queuing delays).  
✅ **Improves throughput** on high-latency or lossy networks (e.g., international connections).  

---

## **🚀 How to Enable BBR on Linux**  

### **1. Check Current Congestion Control**  
```bash
sysctl net.ipv4.tcp_congestion_control
```
(Default: usually `cubic` or `reno`)

### **2. Enable BBR (One-Time)**  
```bash
sudo bash -c 'echo "net.core.default_qdisc=fq" >> /etc/sysctl.conf'
sudo bash -c 'echo "net.ipv4.tcp_congestion_control=bbr" >> /etc/sysctl.conf'
sudo sysctl -p  # Apply changes
```

### **3. Verify BBR is Active**  
```bash
sysctl net.ipv4.tcp_congestion_control  # Should output "bbr"
lsmod | grep bbr  # Check if BBR module is loaded
```

---

## **⚙️ Advanced Tuning (Optional)**  
### **BBR v2/v3 (Kernel ≥5.10+)**  
```bash
# For BBRv2 (if compiled in kernel):
sudo bash -c 'echo "net.ipv4.tcp_congestion_control=bbr2" >> /etc/sysctl.conf'

# For BBRv3 (latest Linux kernels):
sudo bash -c 'echo "net.ipv4.tcp_congestion_control=bbr" >> /etc/sysctl.conf'
```

### **Custom Parameters**  
```bash
# Increase TCP buffer sizes (adjust based on your bandwidth):
echo "net.core.rmem_max=4194304" | sudo tee -a /etc/sysctl.conf
echo "net.core.wmem_max=4194304" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

---

## **📊 Performance Comparison**  
| **Metric**       | **CUBIC (Default)** | **BBR** | **BBRv2/v3** |  
|------------------|---------------------|---------|--------------|  
| **Throughput**  | Moderate            | High    | Very High    |  
| **Latency**     | Variable            | Low     | Very Low     |  
| **Fairness**    | Good                | Better  | Best         |  

---

## **⚠️ Notes & Caveats**  
1. **Kernel Requirement**: BBR requires **Linux 4.9+**. For BBRv2/v3, use **5.10+**.  
   - Check kernel: `uname -r`  
2. **Not All Networks Benefit**: BBR excels in high-latency/lossy networks but may underperform in local LANs.  
3. **Compatibility Issues**: Some outdated middleboxes (e.g., firewalls) may interfere.  

---

## **📚 Further Reading**  
- [Google BBR Paper](https://research.google/pubs/pub45646/)  
- [Kernel Documentation](https://www.kernel.org/doc/Documentation/networking/ip-sysctl.txt)  

---

## **🎯 Why Use This Script?**  
This project (`Ya-MIC BBR Manager`) automates the above steps and adds:  
🔹 **One-click installation** for BBRv1/v2/v3.  
🔹 **Dynamic tuning** based on network conditions.  
🔹 **Support for multiple Linux distros** (Debian/Ubuntu/CentOS).  

**👉 Get Started:**  
```bash
wget https://github.com/Ya-MIC/bbr-manager/install.sh && sudo bash install.sh
```

---

### **License**  
MIT © [Ya-MIC](https://github.com/Ya-MIC)  

---

