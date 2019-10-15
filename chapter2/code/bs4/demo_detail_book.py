#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

response = requests.get('https://www.packtpub.com/application-development/learn-python-programming-second-edition')
soup = BeautifulSoup(response.text,'lxml')

title = soup.find('span', attrs={'data-ui-id':'page-title-wrapper'}).text
author = soup.find('div', attrs={'class':'authors inline'}).text

print(title)
print(author)