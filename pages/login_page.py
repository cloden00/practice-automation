# File: pages/login_page.py

class LoginPage:
    def __init__(self, page):
        # 1. Store the active browser page
        self.page = page
        
        # 2. Define the locators as variables (The "Template" elements)
        self.username_input = page.locator('[data-test="username"]')
        self.password_input = page.locator('[data-test="password"]')
        self.login_button = page.locator('[data-test="login-button"]')
        self.error_message = page.locator('[data-test="error"]')

    # 3. Define the actions you can take on this page
    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_text(self):
        return self.error_message.inner_text()