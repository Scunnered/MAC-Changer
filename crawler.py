#!/usr/bin/env python

import requests

def request(url):
    try:
        return request.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass

target_url = "zsecurity.org"

response = request(target_url)
print(response.content)