##main.py
from fastapi import FastAPI, Depends
from pydantic import BaseModel, ConfigDict
import hmac

app= FastAPI()

def get_username():
    print("Executing get_username dependency")
    return "Alice"

class Message(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str

def get_current_user(username: str = Depends(get_username)):
    return {
        "username": username
    }

def get_greeting(name: str):
    print("Executing get_greeting")
    return f"Hello, {name}!"


@app.get("/greeting")
def greeting(message: str = Depends(get_greeting)):
    return {"message": message}

@app.get("/current-user")
def current_user(user: dict = Depends(get_current_user)):
    print("Executing get_current_user dependency")
    return user

@app.get('/')
def home():
    return {"message": "Hello! My AI Voice Companion server is running."}

@app.get('/hello')
def say_hello():
    return {"message": "Hello from the second endpoint!"}

@app.post('/message')
def receive_message(message: Message):
    return {
        "received": message.text,
        "status": "success"
    }
