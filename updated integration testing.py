#updated integration testing


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class TestLoginIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get("https://university-community-system.vercel.app/")

    @classmethod
    def tearDownClass(cls):
        time.sleep(10) # Requirement: Pause for 10 seconds
        cls.driver.quit()

    def test_login_to_dashboard_flow(self):
        driver = self.driver
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()
            
            # Input credentials
            email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "email")))
            email_input.send_keys("zahir@gmail.com")
            driver.find_element(By.ID, "password").send_keys("demo123")
            driver.find_element(By.XPATH, "//button[@type='submit']").click()

            # Verify modules integrated successfully
            WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))
            self.assertIn("dashboard", driver.current_url)
            print("Integration Test: Login-to-Dashboard flow verified.")
        except Exception as e:
            self.fail(f"Integration test failed: {e}")

if __name__ == "__main__":
    unittest.main()