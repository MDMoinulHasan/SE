#updated unit testing

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class TestLoginFields(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        options.add_argument("--window-size=1920,1080")
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get("https://university-community-system.vercel.app/")

    @classmethod
    def tearDownClass(cls):
        time.sleep(10) # Requirement: Pause for 10 seconds before closing
        cls.driver.quit()

    def test_email_and_password_fields_present(self):
        driver = self.driver
        try:
            login_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_link.click()
            
            # Focused strictly on component presence
            email_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "email"))
            )
            password_field = driver.find_element(By.ID, value="password")
            
            self.assertIsNotNone(email_field, "Email field should be present")
            self.assertIsNotNone(password_field, "Password field should be present")
            print("Unit Test: Login UI components verified.")
        except Exception as e:
            self.fail(f"Unit test failed: {e}")

if __name__ == "__main__":
    unittest.main()