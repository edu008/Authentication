from fastapi import FastAPI, HTTPException, Depends
from werkzeug.security import generate_password_hash, check_password_hash
from pydantic import BaseModel

app = FastAPI()

# Dummy database
users_db = {}

class User(BaseModel):
    username: str
    password: str

@app.post("/register")
def register_user(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user.username] = generate_password_hash(user.password)
    return {"message": "User registered successfully"}

@app.post("/login")
def login(user: User):
    hashed_password = users_db.get(user.username)
    if not hashed_password or not check_password_hash(hashed_password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"message": "Login successful"}
