import socket
import argparse

def scan_port(target, port):
    try:
        # Create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Set a timeout for the connection attempt
        result = s.connect_ex((target, port))  # Attempt to connect
        if result == 0:
            print(f"[+] Port {port} is open")
        s.close()
    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Simple Port Scanner")
    parser.add_argument("target", help="Target IP or domain")
    parser.add_argument("ports", help="Ports to scan (comma-separated)")
    
    args = parser.parse_args()
    
    target = args.target
    ports = [int(port) for port in args.ports.split(",")]

    print(f"Scanning {target} for open ports...\n")
    for port in ports:
        scan_port(target, port)

if __name__ == "__main__":
    main()
