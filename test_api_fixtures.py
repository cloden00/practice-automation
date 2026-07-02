import pytest
import requests

# 1. Define the Fixture
# The @pytest.fixture decorator tells the framework this is an environment manager
@pytest.fixture
def api_client():
    # --- SETUP PHASE ---
    # Prepare the configuration state before the test runs
    base_url = "https://dummyjson.com"
    payload = {"username": "emilys", "password": "baseline_password"}
    
    print("\n[Setup] API baseline configuration allocated.")
    
    # The 'yield' keyword splits the function. 
    # It passes the dictionary to the test and PAUSES execution here.
    yield (base_url, payload)
    
    # --- TEARDOWN PHASE ---
    # This code is GUARANTEED to run after the test finishes, no matter what
    print("[Teardown] Clearing session state and cleaning memory references.")


# 2. Injecting the Fixture
# To use a fixture, you simply pass its function name as an argument to your test.
# Pytest matches the string name and injects the yielded data automatically.
def test_successful_login(api_client):
    base_url, payload = api_client
    
    # Modify the payload for this specific test case
    payload["password"] = "emilyspass"
    
    print("[Test] Executing successful login assertion...")
    response = requests.post(f"{base_url}/auth/login", json=payload)
    
    assert response.status_code == 200
    assert "accessToken" in response.json()


def test_malformed_login_fails(api_client):
    base_url, payload = api_client
    
    # Modify the payload to inject a broken password
    payload["password"] = "wrong_password"
    
    print("[Test] Executing broken credential assertion...")
    response = requests.post(f"{base_url}/auth/login", json=payload)
    
    assert response.status_code == 400