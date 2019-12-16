from datetime import datetime
import socket

server_address = ('localhost', 16789)
max_size = 4096
print("Starting the server at", datetime.now())
print("Waiting for a client to call.")

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #AF_INET-інтернет сокет(іп), SOCK_DGRAM- використовуємо UDP.

server.bind(server_address) #звязуємо

data, client = server.recvfrom(max_size) #recvfrom чекає приходу діаграми

print("At", datetime.now(), client, "said", data)

server.sendto(b"Are you talking to me?", client)
server.close()