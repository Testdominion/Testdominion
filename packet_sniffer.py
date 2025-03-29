from scapy.all import sniff, IP, TCP, Raw
import argparse

# Function to process captured packets
def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = "TCP" if TCP in packet else "Other"

        # Extract raw payload if available
        payload = ""
        if Raw in packet:
            payload = packet[Raw].load.decode(errors="ignore")

        print(f"[+] {src_ip} -> {dst_ip} | Protocol: {protocol}")
        if payload:
            print(f"    Payload: {payload[:100]}...")  # Print first 100 chars of payload

# Argument parsing for filtering by target website IP
parser = argparse.ArgumentParser(description="Network Packet Sniffer with Website Filtering")
parser.add_argument("--target", help="Target website domain to sniff packets for (e.g., example.com)")
args = parser.parse_args()

# Resolve target domain to IP if provided
TARGET_IP = None
if args.target:
    import socket
    try:
        TARGET_IP = socket.gethostbyname(args.target)
        print(f"[*] Resolving {args.target} to {TARGET_IP}")
    except socket.gaierror:
        print("[!] Failed to resolve domain. Sniffing all packets instead.")
        TARGET_IP = None

print("[*] Starting Packet Sniffer... Press Ctrl+C to stop.")

def packet_filter(packet):
    if TARGET_IP:
        return IP in packet and (packet[IP].dst == TARGET_IP or packet[IP].src == TARGET_IP)
    return True  # Capture all packets if no target is specified

sniff(filter="tcp", prn=packet_callback, store=False, lfilter=packet_filter)
