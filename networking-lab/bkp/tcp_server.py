import socket
import time

server_socket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
server_socket.bind(("127.0.0.1", 9000))
server_socket.listen(5)
connection, client_address = server_socket.accept()

print("Connected by:", client_address) 
time.sleep(60)
