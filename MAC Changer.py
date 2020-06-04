#!/usr/bin/env python

import subprocess
import optparse
import re


def get_arguments():
  parser = optparse.OptionParser()
  parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
  parser.add_option("-m", "--mac", dest="new_MAC", help="New MAC address")
  (options, arguments) = return parser.parse_args()
  if not options.interface: 
      parser.error("[-] Please specify an interface, use --help for more information")
  elif not options.new_mac:
      parser.error("[-] Please specify a new MAC, use --help for more information")
  return options

  
def change_mac(interface, new_mac):
  print("[+] Changing MAC address for " + interface + " to " + new_mac")
  subprocess.call(["ifconfig", interface, "down"])
  subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
  subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
#change_mac(options.interface, options.new_mac)

ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
print(ifconfig_result)
        
mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
print(mac_address_search_result.group(0))
