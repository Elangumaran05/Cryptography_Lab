import socket

MITM_HOST = "127.0.0.1"
MITM_PORT = 8000

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 9000

mitm_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mitm_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mitm_server.bind((MITM_HOST, MITM_PORT))
mitm_server.listen(1)

print("MITM Relay started on port 8000")
print("Waiting for Client...")

client_conn, client_address = mitm_server.accept()
print("\nClient connected:", client_address)

client_data = client_conn.recv(1024)
client_message = client_data.decode()
print("\nMITM observed Client message:")
print(client_message)

server_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_conn.connect((SERVER_HOST, SERVER_PORT))

server_conn.send(client_data)
print("\nMessage forwarded to Server")

server_reply = server_conn.recv(1024)
print("\nMITM observed Server reply:")
print(server_reply.decode())

client_conn.send(server_reply)
print("\nReply forwarded to Client")

server_conn.close()
client_conn.close()
mitm_server.close()
print("\nMITM Relay stopped")
