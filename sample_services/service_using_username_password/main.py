import requests

USER_SERVICE_URL = "http://username_password_service:8000"

def main():
    # Benutzer registrieren
    response = requests.post(f"{USER_SERVICE_URL}/register", json={"username": "test", "password": "password"})
    print("Register Response:", response.json())

    # Login durchführen
    login = requests.post(f"{USER_SERVICE_URL}/login", json={"username": "test", "password": "password"})
    print("Login Response:", login.json())

if __name__ == "__main__":
    main()
