import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # Define UI Locators
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-submit")
        self.success_dashboard = (By.ID, "welcome-message")

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_locator(self.username_field)).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def is_login_successful(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.success_dashboard))
            return True
        except:
            return False

if __name__ == "__main__":
    # Setup Headless Chrome for CI/CD environments (like your GitHub Action or Docker)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    try:
        driver.get("https://example.com") # Replace with your target webpage URL
        login = LoginPage(driver)
        
        login.enter_username("admin")
        login.enter_password("password123")
        login.click_login()
        
        if login.is_login_successful():
            print("SUCCESS: Python login automation completed.")
            sys.exit(0)
        else:
            print("FAILURE: Login failed.")
            sys.exit(1)
    finally:
        driver.quit()
