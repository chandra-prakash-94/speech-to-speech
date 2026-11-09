import requests

response = requests.get("http://127.0.0.1:8000/hello")

print("Status Code:", response.status_code)

print("\nAll Response Headers:")

for name, value in response.headers.items():
    print(f"{name}: {value}")

print("\nResponse Body:")
print(response.text)