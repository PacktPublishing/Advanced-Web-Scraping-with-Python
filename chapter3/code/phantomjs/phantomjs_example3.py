from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.PhantomJS("phantomjs.exe")

driver.get("https://httpbin.org/#/HTTP_Methods/post_post")

driver.find_element_by_class_name("opblock-summary-description").click()

try:
	element = WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "btn"),"Try it out"))
	
finally:
	driver.get_screenshot_as_file("image.png")
 
driver.close()