from scapy.all import *
from scapy.layers.dot11 import Dot11, Dot11Beacon

def packet_handler(packet):
    if packet.haslayer(Dot11Beacon):
        ssid = packet[Dot11].info.decode(errors="ignore")  # Get SSID (network name)
        bssid = packet[Dot11].addr2  # Get MAC address of AP
        signal_strength = packet.dBm_AntSignal if hasattr(packet, 'dBm_AntSignal') else "Unknown"
        print(f"📶 SSID: {ssid} | BSSID: {bssid} | Signal: {signal_strength} dBm")

print("🔍 Scanning for Wi-Fi networks... Press CTRL+C to stop.")
sniff(iface="en0", prn=packet_handler, store=0)
