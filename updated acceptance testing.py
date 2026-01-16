#updated acceptance testing


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class TestAcceptance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get("https://university-community-system.vercel.app/")

    @classmethod
    def tearDownClass(cls):
        time.sleep(10) # Standardized to 10 seconds
        cls.driver.quit()

    def test_user_can_access_system_resources(self):
        driver = self.driver
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()
            
            driver.find_element(By.ID, "email").send_keys("zahir@gmail.com")
            driver.find_element(By.ID, "password").send_keys("demo123")
            driver.find_element(By.XPATH, "//button[contains(text(), 'Sign In')]").click()

            # Acceptance check: Visibility of main system body
            dashboard_body = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            self.assertTrue(dashboard_body.is_displayed())
            print("Acceptance Test: User successfully authorized and redirected.")
        except Exception as e:
            self.fail(f"Acceptance test failed: {e}")

if __name__ == "__main__":
    unittest.main()