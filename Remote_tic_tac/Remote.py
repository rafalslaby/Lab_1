import tic_tac_message_pb2
import socket
import struct


def send_message(sock, message):
    s = message.SerializeToString()
    packed_len = struct.pack('>L', len(s))
    packed_message = packed_len + s
    sock.send(packed_message)


def socket_read_n(sock, n):
    buf = ''
    while n > 0:
        data = sock.recv(n)
        if data == '':
            raise RuntimeError('unexpected connection close')
        buf += data
        n -= len(data)
    return buf


def get_response(sock):
    msg = tic_tac_message_pb2.Coordinates()
    len_buf = socket_read_n(sock, 4)
    msg_len = struct.unpack('>L', len_buf)[0]
    msg_buf = socket_read_n(sock, msg_len)
    msg.ParseFromString(msg_buf)
    return msg


def send_coordinates_request(sock, symbol):
    request = tic_tac_message_pb2.Put_symbol()
    request.symbol = symbol
    send_message(sock, request)
    #return get_response(sock)


def send_response(sock, managed_to_put):
    response = tic_tac_message_pb2.Good_choice()
    response.managed_to_put_symbol = managed_to_put
    send_message(sock, response)


def send_coordinates(sock, x, y, symbol):
    coordinates = tic_tac_message_pb2.Coordinates()
    coordinates.x = x
    coordinates.y = y
    coordinates.symbol = symbol
    send_message(sock, coordinates)
