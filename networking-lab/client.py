import requests
import time

url = "http://127.0.0.1:8000/di-test"

# payload = {
#     "text": "Hello!"
# }

response = requests.get(url)
print("Status Code:", response.status_code)
print("Response Body:", response.text)
