import socket

HOST = "127.0.0.1"
PORT = 8000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

message = "Cryptology Lab"
print("Sending message:", message)
client.send(message.encode())

reply = client.recv(1024)
print("Reply from Server:", reply.decode())

client.close()
