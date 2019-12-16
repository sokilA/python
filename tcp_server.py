from datetime import datetime
import socket

server_address = ('localhost', 16789)
max_size = 4096
print("Starting the server at", datetime.now())
print("Waiting for a client to call.")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET-інтернет сокет(іп), SOCK_DGRAM- використовуємо TCP.

server.bind(server_address) #звязуємо
server.listen(5)

client, addr = server.accept()
data = client.recv(max_size)

print("At", datetime.now(), client, "said", data)

client.sendall(b'Are you talking to me?')
client.close()
server.close()