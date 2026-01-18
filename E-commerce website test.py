from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Firefox()

URL='https://www.saucedemo.com/'

driver.get(URL)
driver.maximize_window()
time.sleep(2)
print(driver.title)

#username
driver.find_element(By.ID, value='user-name').clear()
driver.find_element(By.ID, value='user-name').send_keys('error_user')
time.sleep(1)

#password
driver.find_element(By.ID, value='password').clear()
driver.find_element(By.ID, value='password').send_keys('secret_sauce')
time.sleep(.5)

#login
driver.find_element(By.NAME, value='login-button').click()
time.sleep(.5)


#item1
driver.find_element(By.ID, value='add-to-cart-sauce-labs-backpack').click()
time.sleep(1)

#item2
driver.find_element(By.ID, value='add-to-cart-sauce-labs-bike-light').click()
time.sleep(.5)

#cart
driver.find_element(By.CLASS_NAME, value='shopping_cart_link').click()
time.sleep(1)

#remove item
driver.find_element(By.ID, value='remove-sauce-labs-bike-light').click()
time.sleep(.5)

#checkout
driver.find_element(By.ID, value='checkout').click()
time.sleep(2)

#logout
driver.find_element(By.ID, value='react-burger-menu-btn').click()
time.sleep(1)
driver.find_element(By.ID, value='logout_sidebar_link').click()
time.sleep(1)

time.sleep(3)
driver.quit()