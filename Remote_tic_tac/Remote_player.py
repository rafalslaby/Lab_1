import socket
import protoc_pb2
import socket_management as sm
import time


host = 'localhost'
port = 50001
data_size = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (host, port)
sock.connect(server_address)

message = protoc_pb2.msg()

while 1:
    data = sm.get_response(sock)
    if data:
        if data.type == 0:
            print(data.text)
            message.type = int(input())
            sm.send_message(sock, message)
            if message.type == 3:
                break
        if data.type == 1:
            print(data.text)
            message.text = str(input())
            sm.send_message(sock, message)
        if data.type == 2:
            print('-' * 8)
            counter = 0
            for i in data.tab:
                counter += 1
                print(i, end=', ')
                if counter % 3 == 0:
                    print()
            print('-' * 8)
        if data.type == 3:
            message.x = int(input('Choose x coordinate '))
            message.y = int(input('Choose y coordinate '))
            sm.send_message(sock, message)

        if data.type == 4:
            message.x = int(input('In range from: '))
            message.y = int(input('to: '))
            sm.send_message(sock, message)

        if data.type == 5:
            message.guess = int(input('Give your next guess  '))
            sm.send_message(sock, message)

        if data.type == 10:
            print(data.text)
