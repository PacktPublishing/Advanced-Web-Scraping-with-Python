from selenium import webdriver

driver = webdriver.PhantomJS("phantomjs.exe")
driver.get("https://protonmail.com/")
print(driver.find_element_by_class_name("homepage-hero-sub-title").text)