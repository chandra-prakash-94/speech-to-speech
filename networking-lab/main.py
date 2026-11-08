from fastapi import FastAPI

app= FastAPI()

@app.get('/')
def home():
    return {"message": "Hello! My AI Voice Companion server is running."}
