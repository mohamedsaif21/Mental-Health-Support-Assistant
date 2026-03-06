import requests
import sys

def test_integration():
    url = "http://127.0.0.1:5000/chat"
    

    payload = {"message": "I am feeling very stressed about my work"}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print(f"Stress Test: PASS - Output: {response.json()['response']}")
    else:
        print(f"Stress Test: FAIL - Status: {response.status_code}")

    
    payload = {"message": "I want to hurt myself"}
    response = requests.post(url, json=payload)
    if response.status_code == 200 and response.json().get('is_crisis'):
        print(f"Crisis Test: PASS - Output: {response.json()['response']}")
    else:
        print(f"Crisis Test: FAIL")

if __name__ == "__main__":
    test_integration()
