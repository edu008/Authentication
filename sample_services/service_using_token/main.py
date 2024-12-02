import requests

TOKEN_SERVICE_URL = "http://token_service:8000"

def main():
    # Token generieren
    response = requests.post(f"{TOKEN_SERVICE_URL}/token", json={"user_id": "123"})
    token = response.json()["access_token"]

    # Token validieren
    validation = requests.get(f"{TOKEN_SERVICE_URL}/validate", params={"token": token})
    print("Validation Response:", validation.json())

if __name__ == "__main__":
    main()
