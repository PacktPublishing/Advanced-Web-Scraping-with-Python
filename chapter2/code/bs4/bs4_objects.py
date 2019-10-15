#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
header = {'user-agent':ua.chrome}
google_page = requests.get('http://www.packtpub.com',headers=header)

soup = BeautifulSoup(google_page.content,'lxml')

#find parent
print("Parent of the form with id='search_mini_form':")	
parent_form = soup.find("form",{"id":"search_mini_form"}).parent
print(parent_form) 

#get children form a specific element,in this case we are getting child elements of the form with id="search_mini_form"
print("Children of the form with id='search_mini_form:'")
for child in soup.find("form",{"id":"search_mini_form"}).children:
    print(child)

#find next_siblings	
print("Siblings of the form with id='search_mini_form:'")
for sibling in soup.find("form",{"id":"search_mini_form"}).input.next_siblings:
    print(sibling)