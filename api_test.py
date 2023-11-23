import requests

def test_api():
    response = requests.get('https://api.publicapis.org/entries')
    assert response.status_code == 200, f"API call failed with status: {response.status_code}"

if __name__ == "__main__":
    test_api()
    print("API call successful")
