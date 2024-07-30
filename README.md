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
   drop tcp any any -> $HOME_NET any (msg:"Large TCP Packet Detected"; dsize:>1500;classtype:attempted-dos; sid:4; rev:1;)
   ```

5. **Restart Suricata** to apply changes:
   ```bash
   sudo systemctl restart suricata
   ```

## Attack Simulation

### Script 1: Basic SYN Flood Attack

For Attack script click here [first-script.py](first-script.py)

This script sends a continuous stream of SYN packets to simulate a SYN flood attack.untill here only 1st and 2nd rule is configuered so running this scripts launches the attack and also suricata shows alerts : 

**Running The Script**

![sf1](https://github.com/user-attachments/assets/7825a5bc-ea39-4ff3-9f79-9f5225ef8569)

**Suricata Alerts**

![sf2](https://github.com/user-attachments/assets/d4025cca-47ac-43b9-a8c8-5513c159505f)

**Expected Outcome**: Suricata should trigger alerts based on the defined rules for SYN flood detection.

### Script 2: Bypass SYN Flood Detection

For whole script click here [second-script.py](second-script.py)

This script uses random source IPs to evade detection by changing the source address.This acts as a bypass for previous script alerts when 1st and 2nd rules are configuered and running following script will launch an attack but suricata will not show any alerts hence successfully bypassing ips:

**Running Bypass Script**


![sf3](https://github.com/user-attachments/assets/b32c8fc5-7ccd-41f4-9eea-fd6054cab71a)

**No Alerts Generated by Suricata , Hence successfully bypassed**


![sf4](https://github.com/user-attachments/assets/2d6f3574-cc8d-4890-8023-b536082c8204)

Uncommenting 3rd rule and restarting suricata:

![sf5](https://github.com/user-attachments/assets/b246a23a-a9eb-46eb-9c50-6b1888e5f31e)


**Again Running Script:**


![sf6](https://github.com/user-attachments/assets/2602f438-2e81-44db-99e1-8c6769209869)

**Alerts Generated By Suricata**


![sf7](https://github.com/user-attachments/assets/d9324153-6276-49e0-b0d8-2f9a4f6cb0da)


### Script 3: Oversized SYN Packet Attack

For whole script click here [third-script.py](third-script.py)

This script sends oversized SYN packets to test Suricata's ability to handle payloads. It is to bypass previous rules configuered and running following script will launch an attack but suricata will not show any alerts hence successfully bypassing ips:

**Running 3rd Script**

![sf8](https://github.com/user-attachments/assets/5fec7aaf-226f-4f40-9ca7-805b167b7e9d)

**Suricata Shows no alerts**


![sf9](https://github.com/user-attachments/assets/4a7244cb-9b16-4785-bc6f-e9b8c2583b01)

Uncommenting 4th rule and again running the script:

![sf10](https://github.com/user-attachments/assets/fcb56710-eec4-4153-b4a8-b70c0262042c)

**Suricata Shows Alerts:**


![sf11](https://github.com/user-attachments/assets/67c6749f-79fb-429f-bc7f-eec02cc009b1)


**Note:** We can further go and add rules in suricata to show alerts if abnormally large data is recieved and again write bypass script for it.

## Results and Analysis

1. **Basic SYN Flood Attack**: Suricata should generate alerts based on the rules configured.
2. **Bypass SYN Flood Detection**: The effectiveness of evading detection by using random source IPs.
3. **Oversized SYN Packet Attack**: Testing Suricata's ability to handle and alert on oversized packets.

## Conclusion

This project demonstrates the configuration of Suricata for detecting SYN flood attacks and explores various methods to test and bypass detection mechanisms. By leveraging different attack strategies, this simulation highlights the importance of tuning IDS/IPS systems to effectively handle diverse threats.

## Contributions

Contributions are not Welcome without the permission of the author [/Brooj-Nasir]

## License

This project is licensed under the Proprietary License. See the [LICENSE](LICENSE) file for details.


