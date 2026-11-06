import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # UI Locators matching the local index.html dummy page
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-submit")
        self.success_dashboard = (By.ID, "welcome-message")

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_field)
        ).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def is_login_successful(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.success_dashboard)
            )
            return True
        except Exception:
            return False

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        # Resolves path to index.html in the same directory (webpage/)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        html_file = os.path.join(script_dir, "index.html")
        
        # Load local HTML file into browser
        driver.get(f"file://{html_file}")
        
        login = LoginPage(driver)
        
        # Action steps
        login.enter_username("admin")
        login.enter_password("password123")
        login.click_login()
        
        # Verification
        if login.is_login_successful():
            print("SUCCESS: Python login automation completed.")
            sys.exit(0)
        else:
            print("FAILURE: Login failed.")
            sys.exit(1)
    finally:
        driver.quit()