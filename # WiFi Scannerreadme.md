# WiFi Scanner

## Overview
This script scans for nearby WiFi networks and retrieves details such as:
- Network SSID (Name)
- Signal strength
- Security type (WPA, WPA2, etc.)
- Channel information

## Features
- Lists all available WiFi networks
- Shows signal strength (dBm)
- Identifies security protocols
- Detects network channels to help with interference analysis

## Installation
Ensure you have **Python 3** installed. Then, install the required dependencies:
```sh
pip install scapy
```
On Linux, ensure you have the necessary permissions:
```sh
sudo apt install aircrack-ng
```

## Usage
Run the script using:
```sh
python wifi_scanner.py
```
For Linux/macOS, you may need to run it with sudo:
```sh
sudo python wifi_scanner.py
```

## Output
The script displays a list of available WiFi networks along with their details.

## Future Enhancements
- Add filtering options (e.g., show only open networks)
- Export results to a file (CSV/JSON)
- Improve real-time scanning with a GUI interface

## Disclaimer
This tool is for educational and security research purposes only. Do not use it to access networks without permission.

---

For any improvements, feel free to update the script!

