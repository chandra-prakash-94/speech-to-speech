from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict

app= FastAPI()

class Message(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str

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
