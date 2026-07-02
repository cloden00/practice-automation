import requests

def test_api_login():
    invalid_passwords:list = ["wrongpass", "", "1", "emilyspass"]

    print("1. Preparing the JSON payload...\n")
    
    # DummyJSON's open authentication endpoint
    url = "https://dummyjson.com/auth/login"
    
    # DummyJSON requires a 'username' instead of an 'email'
    payload = {
        "username": "emilys",
        "password": "baseline_password"
    }
    
    for invalid_password in invalid_passwords:

        payload["password"] = invalid_password

        print(f"2. Firing POST request directly to {url}")
        response = requests.post(url, json=payload)
        
        print(f"3. Server replied with Status Code: {response.status_code}")
        
        # Validation Logic
        if response.status_code == 200:
            print("  -> SUCCESS: Login accepted.")
            # Grab the first 20 characters of the token so it doesn't flood your terminal
            token = response.json().get('accessToken')
            print(f"  -> Server returned Token: {token[:20]}...\n")
        else:
            print(f"  -> FAILED: Server rejected the payload. Error: {response.text} \n")

if __name__ == "__main__":
    test_api_login()