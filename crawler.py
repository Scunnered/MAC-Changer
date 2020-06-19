#!/usr/bin/env python

import requests
import re
import urlparse


target_url = "https://zsecurity.org/product/realtek-ar8812au-2-4-5-ghz-usb-wireless-adapter/"
target_links = []


def extract_links_from(url)
    response = request.get(url)
    return re.findall('(?:href=")(.+?)"', response.content)


href_links = extract_links_from(target_url)
for link in href_links:
    link = urlparse.urljoin(target_url, link)


    if target_url in link and link not in target_links:
        target_links.append(link)
        print(link)