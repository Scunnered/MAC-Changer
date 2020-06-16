#!/usr/bin/env python
import requests

def download(url):
    get_response = request.get(url)
    print(get_response.content)

download("https://i.ytimg.com/vi/-1qju6V1jLM/maxresdefault.jpg")