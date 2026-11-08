import requests

# Send an HTTP GET request to our FastAPI server
response = requests.get("http://127.0.0.1:8000/")

# Inspect the HTTP response
print("Status Code:", response.status_code)
print("Content-Type:", response.headers["Content-Type"])
print("Response Body:", response.text)