#system testing


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        options = Options()
        # Visualization: do not use headless mode
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get("https://university-community-system.vercel.app/")

    @classmethod
    def tearDownClass(cls):
        import time
        time.sleep(10) # Pause for 10 seconds before closing the browser
        cls.driver.quit()

    def test_dashboard_access(self):
        driver = self.driver
        try:
            # Click Login link
            login_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_btn.click()

            # Check email and password fields
            email_input = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "email"))
            )
            password_input = driver.find_element(By.ID, value="password")
            self.assertIsNotNone(email_input, "Email field should be present")
            self.assertIsNotNone(password_input, "Password field should be present")

            # Enter credentials and submit
            email_input.clear()
            email_input.send_keys("zahir@gmail.com")
            password_input.clear()
            password_input.send_keys("demo123")
            sign_in_button = driver.find_element(
                By.XPATH,
                value="//button[@type='submit' and contains(text(), 'Sign In')]"
            )
            sign_in_button.click()

            # Wait for dashboard and check
            WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))
            self.assertIn(
                "dashboard",
                driver.current_url,
                "Should navigate to dashboard after login"
            )

            # Check for dashboard content (example: check for a known element)
            dashboard_body = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            self.assertIsNotNone(dashboard_body, "Dashboard body should be present")

        except Exception as e:
            self.fail(f"System test failed: {e}")

if __name__ == "__main__":
    unittest.main()