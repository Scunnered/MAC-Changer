#!/usr/bin/env python

import requests
import re
import urlparse


target_url = "https://zsecurity.org"

def extract_links_from(url)
    response = request.get(url)
    return re.findall('(?:href=")(.+?)"', response.content)

href_links = extract_links_from(target_url)
for link in href_links:
    link = urlparse.urljoin(target_url, link)

    if target_url in link:
        print(link)