#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from parsel import Selector

# GET request to packtpub site
response = requests.get('https://www.packtpub.com')

# "response.txt" contain all web page content
selector = Selector(response.text)

# Extracting href attribute from anchor tag <a href="*">
href_links = selector.xpath('//a/@href').getall()

#Extracting src attribute from img tag <img src="*">
image_links = selector.xpath('//img/@src').getall()

print('*****href_links******\n')
print(href_links)


print('*****image_links*****\n')
print(image_links)
