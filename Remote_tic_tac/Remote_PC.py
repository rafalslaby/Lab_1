import socket
import random
host = 'localhost'
port = 50001
data_size = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (host, port)
sock.connect(server_address)

while 1:
    data = sock.recv(data_size)
    if data:
        if data == b'1':
            response = str(random.randint(0, 2))
            sock.send(bytes(response, encoding='utf-8'))
            print("X coordinate of PC choice: ", response)
        elif data == b'2':
            response = str(random.randint(0, 2))
            sock.send(bytes(response, encoding='utf-8'))
            print("Y coordinate of PC choice: ", response)

