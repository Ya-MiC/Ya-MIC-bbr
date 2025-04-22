import os
import sys
import time
import subprocess
import speedtest
import statistics
from datetime import datetime

def check_bbr_enabled():
    """检查BBR是否已启用"""
    try:
        with open('/proc/sys/net/ipv4/tcp_congestion_control', 'r') as f:
            congestion_control = f.read().strip()
        return congestion_control == 'bbr'
    except FileNotFoundError:
        return False

def run_speed_test():
    """执行网络测速"""
    st = speedtest.Speedtest()
    
    print("Testing latency...")
    st.get_best_server()
    latency = st.results.ping
    
    print("Testing download speed...")
    download_speed = st.download() / 1_000_000  # 转换为Mbps
    
    print("Testing upload speed...")
    upload_speed = st.upload() / 1_000_000  # 转换为Mbps
    
    return latency, download_speed, upload_speed

def main():
    if not check_bbr_enabled():
        print("Error: BBR is not enabled. Please enable BBR first.")
        sys.exit(1)
    
    print("""
    BBR Network Speed Test
    ----------------------""")
    
    try:
        latency, download, upload = run_speed_test()
        print(f"\nResults:")
        print(f"Latency: {latency:.2f} ms")
        print(f"Download Speed: {download:.2f} Mbps")
        print(f"Upload Speed: {upload:.2f} Mbps")
    except Exception as e:
        print(f"Error during speed test: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()