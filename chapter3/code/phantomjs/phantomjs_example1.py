from selenium import webdriver

driver = webdriver.PhantomJS("phantomjs.exe")
driver.get("https://www.python.org/")
print(driver.find_element_by_class_name("introduction").text)