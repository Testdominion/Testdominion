import requests
from bs4 import BeautifulSoup
import argparse
import socket
import json

# List of common admin panels
admin_paths = ["/admin", "/login", "/wp-admin", "/cpanel", "/dashboard"]

# List of sensitive files
sensitive_files = ["/robots.txt", "/sitemap.xml", "/config.php"]

# Common ports to scan
common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]

# Function to check for security headers
def check_security_headers(headers):
    missing_headers = []
    required_headers = ["X-Frame-Options", "Content-Security-Policy", "X-XSS-Protection"]

    for header in required_headers:
        if header not in headers:
            missing_headers.append(header)
    
    return missing_headers

# Function to perform a port scan
def scan_ports(target):
    open_ports = []
    for port in common_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except Exception as e:
            pass
    return open_ports

# Function to scan for vulnerabilities
def scan_website(url):
    report = {}
    try:
        if not url.startswith("http"):
            url = "http://" + url  # Ensure correct format

        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Get server details
        server = response.headers.get('Server', 'Unknown')
        powered_by = response.headers.get('X-Powered-By', 'Unknown')
        report["server_details"] = {"Server": server, "Powered By": powered_by}

        # Check for outdated software
        outdated = "No"
        if "Apache/2.2" in server or "PHP/5" in powered_by:
            outdated = "Yes"
        report["outdated_software"] = outdated

        # Find forms (possible SQL Injection/XSS risks)
        forms = soup.find_all('form')
        report["potential_vulnerabilities"] = {"forms_found": len(forms)}

        # Check for security headers
        report["missing_security_headers"] = check_security_headers(response.headers)

        # Scan for exposed admin panels
        exposed_admins = []
        for path in admin_paths:
            full_url = url.rstrip("/") + path
            admin_response = requests.get(full_url)
            if admin_response.status_code == 200:
                exposed_admins.append(full_url)
        report["exposed_admin_panels"] = exposed_admins

        # Scan for common sensitive files
        exposed_files = []
        for file in sensitive_files:
            file_url = url.rstrip("/") + file
            file_response = requests.get(file_url)
            if file_response.status_code == 200:
                exposed_files.append(file_url)
        report["exposed_sensitive_files"] = exposed_files

        # Scan for exposed JavaScript files
        js_files = [script['src'] for script in soup.find_all('script', src=True)]
        report["exposed_js_files"] = js_files

        # Perform port scanning
        target_host = url.replace("http://", "").replace("https://", "").split('/')[0]
        open_ports = scan_ports(target_host)
        report["open_ports"] = open_ports

        # Save report to a file
        with open("scan_report.json", "w") as f:
            json.dump(report, f, indent=4)
        print("\n[+] Scan completed. Report saved to scan_report.json")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Argument parsing for command-line use
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advanced Website Vulnerability Scanner")
    parser.add_argument("url", help="Target website URL (e.g., http://example.com)")
    args = parser.parse_args()

    scan_website(args.url)
