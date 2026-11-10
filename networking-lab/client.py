import requests
import time

url = "http://127.0.0.1:8000/message"

payload = {
    "text": "Hello!"
}

with requests.Session() as session:

    response = session.post(url, json=payload)

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
    print("Connection Header:", response.headers.get("Connection"))
    print("\nAll Response Headers:")
    for key, value in response.headers.items():
        print(f"{key}: {value}")

    print("\nConnection is being kept available.")
    print("Waiting for 30 seconds...")

    time.sleep(60)