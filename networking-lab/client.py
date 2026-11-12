import requests
import time

url = "http://127.0.0.1:8000/products?user_id=103"

response = requests.get(url)
print("Status Code:", response.status_code)
print("Response Body:", response.text)
