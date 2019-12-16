from datetime import datetime
import socket

server_address = ('localhost', 16789)
max_size = 4096
print("Starting the server at", datetime.now())
print("Waiting for a client to call.")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(server_address)
server.listen(5)

client, addr = server.accept()
data = client.recv(max_size)

print("At", datetime.now(), client, "said", data)

client.sendall(b'Questions?')
client.close()
server.close()