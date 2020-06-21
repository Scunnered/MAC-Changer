#!/usr/bin/env python

import requests
import re
import urlparse

class Scanner:
    def _init_(self, url, ignore_links):
        self.session = requests.Session()
        self.target_url = url
        self.target_links = []
        self.links_to_ignore = ignore_links

    def extract_links_from(self, url):
        response = self.requests.get(url)
        return re.findall('(?:href=")(.*?)"', response.conter)

    def crawl(self, url=None):
        if url == None:
            url = self.target_url
        href_links = self.extract_links_from(url)
        for link in href_links:
            link = urlparse.urljoin(url, link)

            if '#' in link:
                link = link.split('#')[0]

            if self.target_url in link and link not in target_links and link not in self.links_to_ignore:
                self.target_links.append(link)
                print(link)
                self.crawl(link)