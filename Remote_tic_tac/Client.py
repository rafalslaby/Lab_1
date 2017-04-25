import socket

host = 'localhost'
port = 50001
data_size = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (host, port)
sock.connect(server_address)

b = bytes("Hello", 'utf-8')

sock.send(b)
while 1:
    b = bytes(str(input("podaj wiadomosc:")), 'utf-8')
    sock.send(b)
    print(sock.recv(data_size))
