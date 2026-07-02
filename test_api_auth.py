import pytest
import requests

# 1. The Data Matrix
# We define a list of tuples: (password_to_test, expected_status_code)
test_data = [
    ("wrongpass", 400),
    ("", 400),
    ("1", 400),
    ("emilyspass", 200)
]

# 2. The Decorator
# This tells Pytest: "Inject the test_data array into the variables 'password' and 'expected_status'"
@pytest.mark.parametrize("password, expected_status", test_data)
def test_login_boundaries(password, expected_status):
    url = "https://dummyjson.com/auth/login"
    
    payload = {
        "username": "emilys",
        "password": password
    }
    
    response = requests.post(url, json=payload)
    
    # 3. The Assertion
    # No if/else statements. We just state what MUST be true.
    # If it is false, Pytest immediately fails this specific run and logs it.
    assert response.status_code == expected_status
    
    # If we expect a 200 OK, we also assert that the server gave us a token
    if expected_status == 200:
        assert "accessToken" in response.json()