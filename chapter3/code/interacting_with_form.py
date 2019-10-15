from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
import time

url = "https://websistent.com/tools/htdigest-generator-tool/"
user = "myUser"

driver = webdriver.Chrome('chromedriver.exe')
driver.get(url)

element = driver.find_element_by_id("uname")
element.send_keys(user)

#If we go to the browser we will see that we have completed the first input of the form. 
#Then fill in the rest of inputs

element = driver.find_element_by_id("realm")
element.send_keys("myRealm")

element = driver.find_element_by_id("word1")
element.send_keys("mypassword")

element = driver.find_element_by_id("word2")
element.send_keys("mypassword")

#Finally, we look for the button and click it
driver.find_element_by_id("generate").click();

# We wait 2 seconds before searching for the item
#time.sleep(2)

try:
    # We wait a maximum of 10 seconds while we wait for the "Loading" text to disappear
    WebDriverWait(driver, 10).until_not(lambda driver: driver.find_element_by_id("output").text.startswith("Loading"))

    output = driver.find_element_by_id("output").text
    print (output[output.find(user):])

except TimeoutException:
    print("The realm could not be generated or the page has taken too long time to load")
	
finally:
    driver.quit()