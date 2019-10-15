#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd

driver = webdriver.Chrome("chromedriver.exe")

driver.get('https://www.packtpub.com/gb/web-development/web-programming')
content = driver.page_source

soup = BeautifulSoup(content,'lxml')

books=[] #List to store book titles
authors=[] #List to store authors
dates=[] #List to store dates


for element in soup.findAll('div', attrs={'class':'card h-100'}):
	title = element.find('h5', attrs={'class':'card-title mt-0'})
	author = element.find('div', attrs={'class':'author-names'})
	meta = element.find('div', attrs={'class':'product-meta'})
	if title is not None:
		print(title.contents[0].strip())
		title_text = title.contents[0].strip()
	else:
		title_text = ''
	
	if author is not None:
		author_text = author.find('p').text
	else:
		author_text = ''
		
	if meta is not None:
		date_text = meta.findChild().text
	else:
		date_text = ''
	
	
	books.append(title_text)
	authors.append(author_text)
	dates.append(date_text)
	
df = pd.DataFrame({'Book title':books,'Author':authors,'Date':dates})
df.to_csv('books.csv', index=False, encoding='utf-8')
