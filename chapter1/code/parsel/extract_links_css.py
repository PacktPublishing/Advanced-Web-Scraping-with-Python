#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from parsel import Selector

# GET request to packtpub site
response = requests.get('https://www.packtpub.com')

# "response.txt" contain all web page content
selector = Selector(response.text)

# Extracting href attribute from anchor tag <a href="*">
href_links = selector.css('a::attr(href)').extract()

#Extracting src attribute from img tag <img src="*">
image_links = selector.css('img::attr(src)').extract()

print('*****************************href_links************************************\n')
print(href_links)


print('*****************************image_links************************************\n')
print(image_links)
