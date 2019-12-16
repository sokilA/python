#udp_client.py

from datetime import datetime
import socket

server_address = ('localhost', 16789)
max_size = 4096
print("starting the client at", datetime.now())

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b"hey!", server_address)
data,server = client.recvfrom(max_size)
print("at", datetime.now(), server, "said", data)
client.close()