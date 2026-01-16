
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
v = Options()
v.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=v)

driver.get('https://practicetestautomation.com/practice-test-login/')

driver.find_element(By.ID, 'username').send_keys('student')
driver.find_element(By.ID, 'password').send_keys("Password123")
driver.find_element(By.ID, 'submit').click()

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Log out')))
print("Login successful!")
driver.find_element(By.LINK_TEXT, 'Log out').click()
print("Logged out successfully.")
time.sleep(10)
driver.close()
