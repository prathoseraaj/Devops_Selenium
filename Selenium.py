from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#setup webdriver(Uses chrome)
driver=webdriver.Chrome()

#opens google
driver.get("https://www.google.com")

#Finds the search box using attribute
search_box=driver.find_element("name","q")

#type search query
search_box.send_keys("Selenium testing in windows")

#simulates entering enter key
search_box.send_keys(Keys.RETURN)

driver.quit()