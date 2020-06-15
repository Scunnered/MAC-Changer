#!/usr/bin/env python
import scapy.all as scapy
from scapy.layer import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.hayslayer(http.HTTPREQUEST):
        if packet.haslayer(scapy.Raw):
            print(packet)

sniff("eth0")