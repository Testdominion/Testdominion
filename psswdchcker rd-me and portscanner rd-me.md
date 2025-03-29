# Port Scanner

## Overview
This script scans a given IP address or domain for open ports, identifying potential security risks. It helps detect services running on a system and assess network security.

## Features
- Scans for open ports on a target IP or domain
- Detects common services running on discovered ports
- Supports scanning specific port ranges
- Provides a detailed scan report

## Installation
Ensure you have **Python 3** installed. Then, install the required dependencies:
```sh
pip install socket python-nmap
```

## Usage
Run the script using:
```sh
python port_scanner.py -t <target_ip> -p <port_range>
```
Example:
```sh
python port_scanner.py -t 192.168.1.1 -p 1-1000
```

## Output
The script lists open ports and the services running on them.

## Future Enhancements
- Implement multi-threading for faster scans
- Add service and version detection

## Disclaimer
This tool is for educational and security research purposes only. Do not use it on systems you do not own or have permission to test.

---

# Password Strength Checker

## Overview
This script evaluates the strength of a given password based on criteria like length, complexity, and common vulnerabilities.

## Features
- Checks password length
- Evaluates the use of uppercase, lowercase, numbers, and special characters
- Detects common passwords and weak patterns
- Provides a strength rating

## Installation
Ensure you have **Python 3** installed. Then, install the required dependencies:
```sh
pip install hashlib
```

## Usage
Run the script using:
```sh
python password_checker.py
```
Enter a password when prompted, and the script will return a strength assessment.

## Output
The script rates the password as **Weak**, **Moderate**, or **Strong**, providing feedback for improvement.

## Future Enhancements
- Add integration with a breached password database
- Implement password entropy calculation

## Disclaimer
This tool is for educational purposes only. Users should follow best security practices for password management.

---

For any improvements, feel free to update the scripts!

