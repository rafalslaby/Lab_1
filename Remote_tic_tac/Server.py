import socket

host = 'localhost'
port = 50001
data_size = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (host, port)
sock.bind(server_address)

sock.listen(1)
connection, client_address = sock.accept()
while True:
    data = connection.recv(data_size)
    if data:
        received_data = bytes.decode(data, encoding='utf-8')
        print(received_data)
        print(type(received_data))
        connection.send(data)
        if received_data == "END":
            break