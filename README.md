# Ethical Hacking with Python
In this repository I will be creating handy to have scripts for aspiring ethical hackers like myself.
You will find below a list of script names, descriptors and why they are needed.

These scripts have been created in PyCharm on Kali Linux on VirtualBox:

Pycharm - https://www.jetbrains.com/pycharm/

Kali - https://www.offensive-security.com/kali-linux-vm-vmware-virtualbox-image-download/#1572305786534-030ce714-cc3b

As stated in the description... each script is for educational use only!

# ARP Spoofing
A program that sends falsified ARP (Address Resolution Protocol) messages over a local area network. This results in the linking of an attacker's MAC address with the IP address of a legitimate computer or server on the network.

Why ARP spoofing is possible
1. Clients accept responses even if they did not send a request.
2. Clients trust response without any form of verification.

# Crawler
A program that systematically browses the Web, crawling subdomains
-Domain before the actual domain name
-part of the main domain
EX:
-subdomain.target.com
-mail.google.com
plus.google.com

# DNS Spoofer
A program that intercepts and modifies Packets using Scapy

Scapy can be used to
-Create packets
-Analyse packets
- Send/receive packets
(Can't be used to intercept packet/flows)

# File Interceptor
Program created as "replace_downloads.py"
MITM - Modifying Data program that intercepts communications between two parties either to secretly eavesdrop or modify traffic traveling between the two.

# Guessing Login Information
a Program called post.py To Guess Login Information

# Keylogger
A program that records keys pressed on the keyboard (OOP) 
- Store logs locally (local keyloggers)
- Reports logs to email or remote server (remote keyloggers)
- Log screenshots
- Starts with system startup

# MAC changer
A program that changes a user's MAC Address

Media Access Control
-Permanent
-Physical
-Unique
Assigned by Manufacturer

Why Change the Mac Address?
1. Increase Anonymity
2. Impersonate other devices
3. Bypass filters

# Malware
Program referred to execute_command.py / download.py
- Download file
- Execute code
- Send report
- Download & execute
- Execute & report
- Download, execute & report

# Packet Sniffer
A program that can that can intercept and log traffic that passes over a digital network or part of a network.

1. Capture data flowing through an interface
2. Filter thid data
3. Display interesting infomration such as
- login info
- visited webites
- images

# Vulnerability Scanner
A program that can discover vulnerabilities in a web application. includes scanner.py, vulnerability scanner and extract_forms.
1. Go into every possible page.
2. look for ways to send data to the web application (URL + Forms)
3. Send payloads to discover Vulnerabilities
4. Analyse the response to check of the website is vulnerable

# Network Scanner
A program that scans devices on a network

Why would you want to scan a network?
1. Discover all devices on the network
2. Display their IP address
3. Display their MAC address

