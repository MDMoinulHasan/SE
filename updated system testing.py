#updated system testing


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class TestSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get("https://university-community-system.vercel.app/")

    @classmethod
    def tearDownClass(cls):
        time.sleep(10) # Pause for 10 seconds
        cls.driver.quit()

    def test_complete_system_access(self):
        driver = self.driver
        try:
            # Full end-to-end navigation
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()
            
            email_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "email")))
            email_input.send_keys("zahir@gmail.com")
            driver.find_element(By.ID, "password").send_keys("demo123")
            driver.find_element(By.XPATH, "//button[@type='submit']").click()

            # System-wide validation
            WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))
            self.assertIn("dashboard", driver.current_url)
            print("System Test: Full application cycle verified.")
        except Exception as e:
            self.fail(f"System test failed: {e}")

if __name__ == "__main__":
    unittest.main()