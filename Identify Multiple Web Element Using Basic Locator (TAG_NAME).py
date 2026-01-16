import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

v = Options()
v.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=v)

driver.get('https://www.grameenphone.com/')

time.sleep(3)

link = driver.find_elements(By.TAG_NAME, value="a")
division = driver.find_elements(By.TAG_NAME, value="div")

print("Total number of <a> tags (links):", len(link))
print("Total number of <div> tags (divisions):", len(division))

time.sleep(5)
driver.close()
