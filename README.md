# Packet Capture and Transfer System

This project consists of a client and server for transferring and saving network packets.

* The captured.pcap is obtained by capturing packets of a certain ip address on the internet sending packets to local ethernet (wifi)

## Client
- Reads packets from a PCAP file
- Sends each packet to the server via HTTP POST
- Triggers packet saving with a GET request

## Server
- Receives packets via POST requests
- Stores packets in memory
- Saves received packets to a new PCAP file on demand

### Usage
1. Start the server: `python server.py`
2. Run the client: `python client.py`

Requirements: requests, pyshark, Flask, scapy
