# SYN Flood Attack Project Documentation

## Overview

This document provides a detailed walkthrough of a SYN flood attack simulation, including setup, Suricata configuration, and Scapy scripts. The goal is to demonstrate how to configure Suricata to detect SYN flood attacks and bypass those detections using various scripts.

## Setup

### Virtual Machines Configuration

1. **Suricata VM (Kali Linux)**
   - **Purpose**: Running Suricata for intrusion detection and prevention.
   - **IP Address**: `192.168.100.50`

2. **Attacker VM (Ubuntu)**
   - **Purpose**: Executing SYN flood attack scripts.
   - **IP Address**: `192.168.100.51`

### Suricata Configuration

1. **Install Suricata** on the Kali Linux VM.
   ```bash
   sudo apt-get update
   sudo apt-get install suricata
   ```
   for whole uricata cpnfiguration and custom rules go to my repository [Brooj-Nasir/Suricata-Custom-Rule-Configuration-on-Ubuntu](Brooj-Nasir/Suricata-Custom-Rule-Configuration-on-Ubuntu)

2. **Edit Suricata Configuration** (`/etc/suricata/suricata.yaml`):
   - Ensure the `HOME_NET` variable includes the IP ranges relevant to your setup.

3. **Add Custom Rules** to `/etc/suricata/rules/local.rules`:

   I added rules one by one i added one and wrote a ttack and bypass script for it than another , here are all rules:
   
   ```local.rules
   drop tcp any any -> $HOME_NET 80 (msg:"Possible SYN Flood Attack"; flags:S; flow:stateless; threshold:type both, track by_src, count 40, seconds 10; classtype:attempted-dos; sid:1; rev:3;)
   drop tcp any any -> $HOME_NET 80 (msg:"SYN Flood Detected"; flags:S; flow:stateless; threshold:type both, track by_src, count 10, seconds 5; classtype:attempted-dos; sid:2; rev:4;)
   drop tcp any any -> $HOME_NET any (msg:"Potential DDoS SYN flood - multiple sources"; flags:S; threshold: type both, track by_dst, count 40, seconds 10; sid:3; rev:5;)
   ```

5. **Restart Suricata** to apply changes:
   ```bash
   sudo systemctl restart suricata
   ```

## Attack Simulation

### Script 1: Basic SYN Flood Attack

This script sends a continuous stream of SYN packets to simulate a SYN flood attack.untill here only 1st and 2nd rule is configuered so running this scripts launches the attack and also suricata shows alerts : 

For Attack script click here [first-script.py](first-script.py)

**Expected Outcome**: Suricata should trigger alerts based on the defined rules for SYN flood detection.

### Script 2: Bypass SYN Flood Detection

This script uses random source IPs to evade detection by changing the source address.This acts as a bypass for previous script alerts when 1st and 2nd rules are configuered and running following script will launch an attack but suricata will not show any alerts hence successfully bypassing ips:


For whole script click here [second-script.py](second-script.py)

after configuring 3rd rule suricata will show alerts on it too:



### Script 3: Oversized SYN Packet Attack

This script sends oversized SYN packets to test Suricata's ability to handle payloads. It is to bypass previous rules configuered and running following script will launch an attack but suricata will not show any alerts hence successfully bypassing ips:

For whole script click here [third-script.py](third-script.py)

**Note:** We can further go and add rules in suricata to show alerts if abnormally large data is recieved and again write bypass scriipt for it.
## Results and Analysis

1. **Basic SYN Flood Attack**: Suricata should generate alerts based on the rules configured.
2. **Bypass SYN Flood Detection**: The effectiveness of evading detection by using random source IPs.
3. **Oversized SYN Packet Attack**: Testing Suricata's ability to handle and alert on oversized packets.

## Conclusion

This project demonstrates the configuration of Suricata for detecting SYN flood attacks and explores various methods to test and bypass detection mechanisms. By leveraging different attack strategies, this simulation highlights the importance of tuning IDS/IPS systems to effectively handle diverse threats.

---
