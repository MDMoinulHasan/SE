#Perform Search Operation by Basic Locator (Name)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

v = Options()
v.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=v)

driver.get('https://www.google.com')

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("flower")
search_box.send_keys(Keys.RETURN)

time.sleep(30)
driver.quit()

