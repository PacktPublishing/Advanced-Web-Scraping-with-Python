#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urljoin
import re
import requests

def download_page(url):
    return requests.get(url).text

def extract_links(page):
    link_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    return link_regex.findall(page)

def extract_image_locations(page):
    img_regex = re.compile('<img[^>]+src=["\'](.*?)["\']', re.IGNORECASE)
    return img_regex.findall(page)


if __name__ == '__main__':
    target_url = 'http://www.packtpub.com'
    packtpub = download_page(target_url)
    links = extract_links(packtpub)

    for link in links:
        print(urljoin(target_url, link))

        image_locations = extract_image_locations(packtpub)

    for src in image_locations:
        print(urljoin(target_url, src))
