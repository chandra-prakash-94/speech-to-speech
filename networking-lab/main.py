##main.py
from fastapi import FastAPI, Depends
from pydantic import BaseModel, ConfigDict
import hmac

app= FastAPI()
class Message(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str

def get_username():
    print("Executing get_username dependency")
    return "Alice"

def get_current_user(username: str = Depends(get_username)):
    return {
        "username": username
    }

@app.get("/users/{user_id}")
def get_user(user_id: int):
    print(f"Received user_id: {user_id}")
    return {"user_id": user_id}

@app.get("/products")
def get_products(user_id: int):
    print(f"Received user_id: {user_id}")
    return {"user_id": user_id}

@app.get("/current-user")
def current_user(user: dict = Depends(get_current_user)):
    print("Executing get_current_user dependency")
    return user

@app.post('/message')
def receive_message(message: Message):
    return {
        "received": message.text,
        "status": "success"
    }

@app.get("/conversations")
def get_conversations(user_id: int, limit:int=20):
    print(f"Received user id: {user_id}")
    return {
        "user_id" : user_id,
        "limit": limit
    }
