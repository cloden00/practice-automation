from playwright.sync_api import sync_playwright

# Your array of edge cases. Swag Labs has specific test accounts we can use.
test_users = ["locked_out_user", "invalid_user", "", "standard_user"]

def run_data_driven_test():
    with sync_playwright() as p:
        # slow_mo=500 intentionally slows the execution by half a second so you can watch it type
        browser = p.chromium.launch(headless=False, slow_mo=100)
        
        for user in test_users:
            print(f"Testing Login for: '{user}'")
            
            # Open a fresh incognito context for EVERY loop to ensure cookies are cleared
            context = browser.new_context()
            page = context.new_page()
            
            page.goto("https://www.saucedemo.com/")
            
            # 1. Target the inputs and fill them
            page.locator('[data-test="username"]').fill(user)
            page.locator('[data-test="password"]').fill("secret_sauce") 
            
            # 2. Click the login button
            page.locator('[data-test="login-button"]').click()
            
            # 3. The Validation Logic
            if page.url == "https://www.saucedemo.com/inventory.html":
                print("  -> SUCCESS: Bypassed login and reached dashboard.\n")
            else:
                # If login failed, scrape the exact red error message from the UI
                error_msg = page.locator('[data-test="error"]').inner_text()
                print(f"  -> EXPECTED BLOCK: {error_msg}\n")
                
            # Close this specific tab before the next loop starts
            context.close()
            
        browser.close()

if __name__ == "__main__":
    run_data_driven_test()