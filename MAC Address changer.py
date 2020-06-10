#!/usr/bin/env python

import subprocess
import optparse
import re


def get_arguments(): 
  parser = optparse.OptionParser()
  parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address") #terminal side promts to guide user
  parser.add_option("-m", "--mac", dest="new_MAC", help="New MAC address")
  (options, arguments) = parser.parse_args()
  if not options.interface: 
      parser.error("Specify an interface like wlan0 or eth0, use --help for more information")
  elif not options.new_mac:
      parser.error("Specify a new MAC, use --help for more information")
  return options

  
def change_mac(interface, new_mac):
  print("Changing MAC address for " + interface + " to " + new_mac)
  subprocess.call(["ifconfig", interface, "down"]) #closes MAC instances
  subprocess.call(["ifconfig", interface, "hw", "ether", new_mac]) #enables edits of MAC address
  subprocess.call(["ifconfig", interface, "up"]) #establishes MAC address with custom MAC
  
        
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])        
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result) #rule created on https://pythex.org/

    if mac_address_search_result:
      return mac_address_search_result.group(0)
    else:
      print("MAC address unreadable.") #if user specifed lo as an interface


options = get_arguments() 
        
current_mac = get_current_mac(options.interface)
print("Current MAC = " + str(current_mac)) # returns current MAC

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
if current_mac == option.new_mac:
      print("Mac address was successfully changed to " + current_mac) #confirms if MAC has been changed
else:
      print("MAC address was not changed.") #confirms if MAC has not been changed
