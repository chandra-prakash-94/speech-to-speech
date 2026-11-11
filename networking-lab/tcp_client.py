import socket
import time

client_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

client_socket.connect(("127.0.0.1", 9000))

print("Connected to TCP server!")
time.sleep(60)
