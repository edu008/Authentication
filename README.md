
# Authentication Service

Ein Authentifizierungsservice-Projekt, das Token-basierte und Benutzername-/Passwort-basierte Authentifizierung kombiniert. Dieses Projekt ermöglicht Benutzerregistrierung, Login und Token-Verwaltung in einer Docker-Umgebung.

## Features
- **Benutzerregistrierung:** Erstellen neuer Benutzer mit Benutzernamen und Passwort.
- **Login:** Überprüfung der Anmeldeinformationen.
- **Token-Generierung:** Erstellung von JWT-Tokens für authentifizierte Benutzer.
- **Token-Validierung:** Überprüfung von Tokens zur Autorisierung.

---

## Voraussetzungen
- **Docker**: Installiert und konfiguriert auf deinem System.
- **Docker Compose**: Zum Verwalten der Container.
- **Postman** (oder ein ähnliches API-Tool): Zum Testen der API-Endpunkte.

---

## Installation und Start des Projekts

1. **Repository klonen:**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```

2. **Docker-Container starten:**
   ```bash
   docker-compose up --build
   ```
   - Dies baut die Container und startet den Service.
   - Der Service läuft unter `http://localhost:8001`.

3. **API-Dokumentation ansehen:**
   - Öffne `http://localhost:8001/docs` in deinem Browser.
   - Hier findest du interaktive API-Dokumentationen (Swagger UI).

---

## Nutzung

### API-Endpunkte testen
Zum Testen der Endpunkte kannst du **Postman** verwenden. Hier sind die Schritte:

1. **Postman installieren:** [Postman Download](https://www.postman.com/downloads/)
2. **Neuen Request erstellen:** Wähle den entsprechenden HTTP-Endpunkt aus der folgenden Liste.
3. **Methode auswählen:** Setze die Methode (z. B. POST, GET) gemäß der Beschreibung des Endpunkts.
4. **Headers und Body:** Füge die entsprechenden Daten hinzu (siehe unten).
5. **Request senden:** Überprüfe die Antwort und prüfe, ob der Service wie erwartet funktioniert.

### Endpunkte

#### 1. **Benutzer registrieren**
- **URL:** `http://localhost:8002/register`
- **Methode:** `POST`
- **Body (JSON):**
  ```json
  {
    "username": "User",
    "password": "Passwort"
  }
  ```
- **Erwartete Antwort:**
  ```json
  {
    "message": "User registered successfully"
  }
  ```

#### 2. **Benutzer einloggen**
- **URL:** `http://localhost:8002/login`
- **Methode:** `POST`
- **Body (JSON):**
  ```json
  {
    "username": "User",
    "password": "Passwort"
  }
  ```
- **Erwartete Antwort:**
  ```json
  {
    "access_token": "<generated_jwt_token>"
  }
  ```

#### 3. **Token generieren**
- **URL:** `http://localhost:8001/token`
- **Methode:** `POST`
- **Query-Parameter:**
  - **Key:** `user_id`
  - **Value:** `testuser`
- **Beispiel-URL:**
  ```
  http://localhost:8001/token?user_id=testuser
  ```
- **Erwartete Antwort:**
  ```json
  {
    "access_token": "<generated_jwt_token>"
  }
  ```

#### 4. **Token validieren**
- **URL:** `http://localhost:8001/validate`
- **Methode:** `GET`
- **Query-Parameter:**
  - **Key:** `token`
  - **Value:** `<generated_jwt_token>`
- **Beispiel-URL:**
  ```
  http://localhost:8001/validate?token=<generated_jwt_token>
  ```
- **Erwartete Antwort (gültiger Token):**
  ```json
  {
    "user_id": "User",
    "expires_at": 1733251781
  }
  ```
- **Fehler bei ungültigem Token:**
  ```json
  {
    "detail": "Invalid token"
  }
  ```

---

