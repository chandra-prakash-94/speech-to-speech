from fastapi import FastAPI

app= FastAPI()

@app.get('/')
def home():
    return {"message": "Hello! My AI Voice Companion server is running."}

@app.get('/hello')
def say_hello():
    return {"message": "Hello from the second endpoint!"}