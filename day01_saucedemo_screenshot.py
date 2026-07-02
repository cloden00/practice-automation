from playwright.sync_api import sync_playwright

def test_environment_setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com/")
        
        # This halts the script completely. 
        page.pause()
        
        # browser.close()

if __name__ == "__main__":
    test_environment_setup()