#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re

def getLinks(url):
	html = requests.get("http://en.wikipedia.org"+url).text
	bs = BeautifulSoup(html, "html.parser")
	return bs.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

print("Main links from http://en.wikipedia.org//wiki/Python_(programming_language)")
links_level1 = getLinks("/wiki/Python_(programming_language)")

index =0

for link in links_level1:
	
	print("http://en.wikipedia.org"+link.get('href').encode('utf-8'))
	
	newLink= links_level1[index].attrs["href"]
	
	links_level2 = getLinks(newLink)
	
	print("Links from http://en.wikipedia.org"+ newLink)
	
	for link in links_level2:
		print("http://en.wikipedia.org"+link.get('href').encode('utf-8'))
		
	index = index +1
	