#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import sys
from selenium import webdriver
import time

#Example input to enter : en (= english)
convert_from = input("Language to Convert from : ")

#Example input to enter : es (= spanish)
convert_to = input("Language to Convert to : ")

text_to_convert = input("Text to translate: ")

#replace spaces by + symbol
text_to_convert = text_to_convert.replace(' ', '+')

#call translate service
url = 'https://translate.google.com/?sl=%s&tl=%s&text=%s' % (convert_from, convert_to, text_to_convert)

browser = webdriver.Chrome("chromedriver.exe")
browser.get(url)

time.sleep(5)

translation = browser.find_element_by_class_name("tlid-translation")
translation2 = browser.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/span[1]/span")

print("Text translated : ", translation2.text)

browser.get_screenshot_as_file('google_translate.png')
browser.close()
