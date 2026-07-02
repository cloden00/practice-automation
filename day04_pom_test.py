# File: day4_pom_test.py

from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage  # Import your template

test_users = ["locked_out_user", "invalid_user", "", "standard_user"]

def run_tests():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        
        for user in test_users:
            print(f"Testing Login for: '{user}'")
            
            context = browser.new_context()
            page = context.new_page()
            
            # 1. Initialize your template for this specific page
            login_page = LoginPage(page)
            
            # 2. Use the template's built-in actions
            login_page.navigate()
            login_page.login(user, "secret_sauce")
            
            # 3. Execute the validation logic
            if page.url == "https://www.saucedemo.com/inventory.html":
                print("  -> SUCCESS: Reached dashboard.\n")
            else:
                print(f"  -> EXPECTED BLOCK: {login_page.get_error_text()}\n")
                
            context.close()
            
        browser.close()

if __name__ == "__main__":
    run_tests()