import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

v = Options()
v.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=v)

driver.get('https://www.grameenphone.com/')

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'swiper-slide'))
)
c = driver.find_elements(By.CLASS_NAME, 'swiper-slide')
print("Number of swiper-slide elements found:", len(c))

time.sleep(5)
driver.close()

