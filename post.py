#!/usr/bin/env python

import requests

targeted_url = "http://10.0.2.20/dvwa/login.php"
data_dict = {"username": "admin", "password": "login": "submit"}
response = request.post(targeted_url, data=data_dict)
print(response.content)