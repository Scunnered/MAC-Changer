#!/usr/bin/env python
import requests

def download(url):
    get_response = request.get(url)
    file_name = url.split("-/-")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

download("https://i.ytimg.com/vi/-1qju6V1jLM/maxresdefault.jpg")