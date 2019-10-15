#!/usr/bin/env python
# -*- coding: utf-8 -*-

from robobrowser import RoboBrowser

browser = RoboBrowser(history=True,parser="html.parser")
browser.open("http://bing.com")
#print(browser.parsed)

#Find the element by id,action or css class in the html
#form = browser.get_form(id = "sb_form")
form = browser.get_form(action="/search")
#form = browser.get_form(class_='sw_box hassbi')

print(form)

form.fields['q'].value = "python"
#form["q"].value = "python"

browser.submit_form(form)

print('*****browser.find_all("a")******\n')

links = browser.find_all("a")
for link in links:
	try:
		print(link['href'])
	except Exception as exception:
		pass