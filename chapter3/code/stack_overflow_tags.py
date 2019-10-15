from selenium import webdriver

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://stackoverflow.com/tags")
tags = driver.find_elements_by_class_name("post-tag")
for i in range(len(tags)):
	print(tags[i].text)