import socket

HOST = "127.0.0.1"
PORT = 9000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen(1)

print("Test Server started on port 9000")
print("Waiting for MITM relay...")

conn, address = server.accept()
print("Connection received from:", address)

data = conn.recv(1024)
message = data.decode()
print("Message received at Server:", message)

reply = "Hello Client, message received by Server"
conn.send(reply.encode())

conn.close()
server.close()
