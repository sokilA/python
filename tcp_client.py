#tcp_client.py

from datetime import datetime
import socket

server_address = ('localhost', 16789)
max_size = 4096
print("starting the client at", datetime.now())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(server_address)
client.sendall(b'Hey!!!')
data = client.recv(max_size)
print('At', datetime.now(), 'someone replied', data)
client.close()
