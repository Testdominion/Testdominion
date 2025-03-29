# Packet Sniffer

## Overview
This script captures and analyzes network packets in real-time. It provides insights into:
- Source and destination IP addresses
- Packet protocols (TCP, UDP, ICMP, etc.)
- Payload data (if available)
- Packet size and timestamps

## Features
- Captures network packets in real-time
- Filters packets based on protocol
- Displays packet details including headers and payloads
- Can save captured data for further analysis

## Installation
Ensure you have **Python 3** installed. Then, install the required dependencies:
```sh
pip install scapy
```
On Linux/macOS, run the script with administrator privileges:
```sh
sudo python packet_sniffer.py
```

## Usage
Run the script with:
```sh
python packet_sniffer.py
```
To filter by protocol (e.g., TCP):
```sh
python packet_sniffer.py --filter tcp
```

## Output
The script displays captured packets with details such as:
```
[Timestamp] SRC_IP -> DEST_IP [Protocol] Data_Size
```

## Future Enhancements
- Add support for saving packets to a **PCAP** file for Wireshark analysis
- Implement a GUI-based packet analysis tool
- Enable advanced filtering by port and application

## Disclaimer
This tool is for educational and security research purposes only. Do not use it to intercept traffic without authorization.

