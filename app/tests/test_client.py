"""Test client for manually testing the API"""
import requests
import json

BASE_URL = "http://localhost:8000"

def print_response(response):
    """Print the response details"""
    print(f"Status code: {response.status_code}")
    print(f"Headers: {json.dumps(dict(response.headers), indent=2)}")
    try:
        print(f"Body: {json.dumps(response.json(), indent=2)}")
    except json.JSONDecodeError:
        print(f"Body: {response.text}")

def test_root():
    """Test the root endpoint"""
    response = requests.get(f"{BASE_URL}/")
    print_response(response)

def test_company_profile(symbol="VNM"):
    """Test the company profile endpoint"""
    response = requests.get(f"{BASE_URL}/api/v1/companies/{symbol}/profile")
    print_response(response)

def test_company_officers(symbol="VNM"):
    """Test the company officers endpoint"""
    response = requests.get(f"{BASE_URL}/api/v1/companies/{symbol}/officers")
    print_response(response)

def test_company_shareholders(symbol="VNM"):
    """Test the company shareholders endpoint"""
    response = requests.get(f"{BASE_URL}/api/v1/companies/{symbol}/shareholders")
    print_response(response)

def test_company_insider_trading(symbol="VNM"):
    """Test the company insider trading endpoint"""
    response = requests.get(f"{BASE_URL}/api/v1/companies/{symbol}/insider-trading")
    print_response(response)

def test_company_subsidiaries(symbol="VNM"):
    """Test the company subsidiaries endpoint"""
    response = requests.get(f"{BASE_URL}/api/v1/companies/{symbol}/subsidiaries")
    print_response(response)

def test_company_events(symbol="VNM"):
    """Test the company events endpoint"""
    response = requests.get(f"{BASE_URL}/api/v1/companies/{symbol}/events")
    print_response(response)

def test_company_news(symbol="VNM"):
    """Test the company news endpoint"""
    response = requests.get(f"{BASE_URL}/api/v1/companies/{symbol}/news")
    print_response(response)

def test_company_dividends(symbol="VNM"):
    """Test the company dividends endpoint"""
    response = requests.get(f"{BASE_URL}/api/v1/companies/{symbol}/dividends")
    print_response(response)

if __name__ == "__main__":
    # Uncomment the tests you want to run
    test_root()
    test_company_profile()
    # test_company_officers()
    # test_company_shareholders()
    # test_company_insider_trading()
    # test_company_subsidiaries()
    # test_company_events()
    # test_company_news()
    # test_company_dividends() 