#!/usr/bin/env python

import requests

url = "plusasdasdasd.google.com"

def request(url):
    try:
        return request.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "google.com"

with open("/root/downloads/subdomains.list", "r") as wordlist_file
    for line in wordlist_file:
        word = line.strip()
        test_url = word + "." + target_url
        response = request(test_url)
        if response:
            print("-/- Discovered Subdomain " + test_url)