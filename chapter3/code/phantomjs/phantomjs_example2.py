from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.PhantomJS("phantomjs.exe")

browser.get("https://www.python.org/")
page = BeautifulSoup(browser.page_source,"html.parser")
links = page.findAll("a")

for link in links:
	print(link.get('href'))

browser.close()