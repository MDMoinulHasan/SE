import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

v = Options()
v.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=v)

driver.get('https://www.facebook.com/')

time.sleep(2)

driver.find_element(By.CSS_SELECTOR, 'input#email').send_keys('abc@example.com')

driver.find_element(By.CSS_SELECTOR, 'input[name="email"]').clear()  # Clear before sending again
driver.find_element(By.CSS_SELECTOR, 'input[name="email"]').send_keys('abc2@example.com')

driver.find_element(By.CSS_SELECTOR, 'input#pass').send_keys('123456')
time.sleep(5)

driver.close()
print("Script ran successfully")
