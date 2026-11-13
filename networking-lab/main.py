##main.py
from fastapi import FastAPI, Depends
from pydantic import BaseModel, ConfigDict
import hmac

app= FastAPI()
class Message(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str

def get_shared_user():
    print("Executing shared user.")
    return {"username" : "Alice"}

def get_username():
    print("Executing get_username dependency")
    return "Alice"

def get_current_user(username: str = Depends(get_username)):
    return {
        "username": username
    }

def get_user_info(user_id: int):
    print("Executing get_user_info")
    print(f"Received user_id: {user_id}")
    return {"user_id": user_id}

def get_conversation(conversation_id: int,user_id: int):
    print("Executing get_conversation")
    print("Conversation ID:", conversation_id)
    print("User ID:", user_id)
    return {
        "conversation_id": conversation_id,
        "user_id": user_id
    }

def get_user_profile(user: dict = Depends(get_shared_user)):
    print("Executing get_user_profile")
    return user

def get_user_settings(user: dict = Depends(get_shared_user)):
    print("Executing get_user_settings")
    return user

@app.get("/user-info/{user_id}")
def user_info(user: dict = Depends(get_user_info)):
    return user

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

@app.get("/conversations/{conversation_id}")
def conversation(data: dict = Depends(get_conversation)):
    return data

@app.get("/profile")
def get_profile(user:dict = Depends(get_shared_user)):
    return {"profile": user}

@app.get("/settings")
def get_settings(user:dict = Depends(get_shared_user)):
    return {"settings_for": user}

@app.get("/user-dashboard")
def user_dashboard(profile: dict = Depends(get_user_profile),settings: dict = Depends(get_user_settings, use_cache=False)):
    return {
        "profile": profile,
        "settings": settings
    }
