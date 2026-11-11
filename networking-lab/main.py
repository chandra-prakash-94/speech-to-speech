##main.py
from fastapi import FastAPI, Depends
from pydantic import BaseModel, ConfigDict
import hmac

app= FastAPI()

def get_username():
    return "Alice"

class Message(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str

@app.get('/di-test')
def di_test(username: str = Depends(get_username)):
    return {
        "username": username
    }

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
