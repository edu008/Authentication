# main.py

from fastapi import FastAPI, Query, HTTPException
from auth import create_token, validate_token

app = FastAPI()

@app.post("/token")
def generate_token(user_id: str = Query(...)):
    """
    Generiert einen JWT-Token.
    """
    token = create_token(user_id)
    return {"access_token": token}

@app.get("/validate")
def validate_token_endpoint(token: str = Query(...)):
    """
    Validiert einen JWT-Token.
    """
    payload = validate_token(token)
    return {"user_id": payload.get("sub"), "expires_at": payload.get("exp")}
