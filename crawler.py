#!/usr/bin/env python

import requests

url = "plusasdasdasd.google.com"
try:
    get_response = request.get("http://" + url)
    print(get_response)
except requests.exceptions.ConnectionError:
    pass