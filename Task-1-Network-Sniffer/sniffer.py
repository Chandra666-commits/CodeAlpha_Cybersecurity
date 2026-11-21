from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime
import csv
import os

OUTPUT_FILE = "output/packet_log.csv"

os.makedirs("output", exist_ok=True)

def analyze_packet(packet, writer, file):
    if IP not in packet:
        return

    ip = packet[IP]
    protocol = "Other"
    source_port = ""
    destination_port = ""

    if TCP in packet:
        protocol = "TCP"
        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport

    elif UDP in packet:
        protocol = "UDP"
        source_port = packet[UDP].sport
        destination_port = packet[UDP].dport

    elif ICMP in packet:
        protocol = "ICMP"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    writer.writerow([
        timestamp,
        ip.src,
        ip.dst,
        protocol,
        source_port,
        destination_port
    ])

    file.flush()

    print(f"[{protocol}] {ip.src} -> {ip.dst}")

print("[+] CodeAlpha Network Sniffer")
print("[+] CSV logging enabled")
print("[+] Capturing 20 IP packets on eth0")

try:
    with open(OUTPUT_FILE, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Timestamp",
            "Source IP",
            "Destination IP",
            "Protocol",
            "Source Port",
            "Destination Port"
        ])

        sniff(
            iface="eth0",
            filter="ip",
            prn=lambda packet: analyze_packet(packet, writer, file),
            count=20,
            store=False
        )

    print(f"[+] Capture completed: {OUTPUT_FILE}")

except KeyboardInterrupt:
    print("[+] Capture stopped by user.")

except Exception as error:
    print(f"[-] Error: {error}")

