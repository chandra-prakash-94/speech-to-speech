def get_resource():
    print("Opening resource...")
    yield "My Resource"
    print("Closing resource...")

resource = get_resource()
print("Resource function created")
value = next(resource)
print(f"Received: {value}")
next(resource)

