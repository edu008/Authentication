# auth.py

import jwt
import time
from fastapi import HTTPException, status
from utils import SECRET_KEY, ALGORITHM, TOKEN_EXPIRATION_TIME

def create_token(user_id: str) -> str:
    """
    Erstellt einen JWT-Token für den angegebenen Benutzer.
    """
    payload = {
        "sub": user_id,
        "exp": time.time() + TOKEN_EXPIRATION_TIME  # Ablaufzeit in Sekunden
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def validate_token(token: str) -> dict:
    """
    Validiert einen JWT-Token.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired",
            headers={"WWW-Authenticate": "Bearer"},
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
