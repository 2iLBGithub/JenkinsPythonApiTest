import requests

def test_api():
    response = requests.get('https://api.publicapis.org/entries')
    assert response.status_code == 200, f"Oh no! Not again! Your API call failed with status: {response.status_code}. Do not give up! Maybe."

if __name__ == "__main__":
    test_api()
    print("Well done! Your API call was successful. You should be VERY proud of yourself.")
