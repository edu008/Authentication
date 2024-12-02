from fastapi import FastAPI, HTTPException, Depends
import jwt
import time
from pydantic import BaseModel

app = FastAPI()

SECRET_KEY = "secure_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_SECONDS = 3600

class TokenData(BaseModel):
    sub: str
    exp: float

def create_token(data: dict):
    data['exp'] = time.time() + ACCESS_TOKEN_EXPIRE_SECONDS
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return TokenData(**payload)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.post("/token")
def generate_token(user_id: str):
    token = create_token({"sub": user_id})
    return {"access_token": token}

@app.get("/validate")
def validate_token(token: str):
    token_data = verify_token(token)
    return {"user_id": token_data.sub, "expires_at": token_data.exp}
