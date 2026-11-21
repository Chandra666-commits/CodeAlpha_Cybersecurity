#CodeAlpha – Basic Network Sniffer

Created by: Chandra Prakash Chandra

##Project Overview

A Python-based network packet sniffer developed using Scapy as part of the CodeAlpha Cybersecurity Internship.

The project captures live IPv4 network packets, analyzes their protocols, identifies source and destination IP addresses, extracts port information, and stores packet details in a CSV file.

##Features

- Live network packet capture
- Source and destination IP identification
- TCP, UDP, and ICMP protocol detection
- Source and destination port identification
- Timestamp recording
- CSV packet logging
- Capture limit of 20 packets per execution

##Technologies Used

- Kali Linux
- Python 3
- Scapy
- CSV module

##Project Structure

Task-1-Network-Sniffer/
├── sniffer.py
├── README.md
├── requirements.txt
├── output/
│   └── packet_log.csv
└── screenshots/

##Prerequisites

- Kali Linux or another compatible Linux distribution
- Python 3
- Scapy
- Root privileges for packet capture

Installation

##Install dependencies:

pip install -r requirements.txt

##Execution

sudo python3 sniffer.py

Note: The current implementation captures packets on the "eth0" network interface.

##Testing and Results

Successfully tested on Kali Linux.

- Captured 20 IPv4 packets.
- Identified source and destination IP addresses.
- Detected UDP traffic and recorded port numbers.
- Recorded packet timestamps.
- Exported packet information to CSV.

##Output

Captured packet information is saved in:

output/packet_log.csv

CSV fields include timestamp, source IP, destination IP, protocol, source port, and destination port.

##Screenshots

Project execution and packet capture screenshots are available in the "screenshots/" directory.

##Limitations

- Currently configured for "eth0".
- Supports IPv4 packet analysis only.
- Captures a maximum of 20 packets per execution.
- Other protocols are classified as "Other".

##Disclaimer

This project is developed strictly for educational purposes and authorized network monitoring only.



