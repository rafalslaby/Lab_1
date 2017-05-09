from Board import Board
import random
import socket
import socket_management as sm
import protoc_pb2


class TicTacToeGame:
    def __init__(self):
        self.board = Board()
        self.game = True
        self.you_go_first = True
        self.player_symbol = 'X'
        self.playerPCsymbol = 'X'

    def start_game(self):
        host = 'localhost'
        port = 50001
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (host, port)
        sock.bind(server_address)
        sock.listen(1)
        connection, client_address = sock.accept()

        while True:
            msg = protoc_pb2.msg()
            msg.type = 0
            msg.text = 'Which game do you wanna play? \n1 - for tic tac toe\n2 - for more or less\n3 - quit'
            sm.send_message(connection, msg)
            msg = sm.get_response(connection)
            if msg.type == 3:
                break
            if msg.type == 1:
                while True:
                    msg.type = 1
                    msg.text = 'Choose your symbol: x or o '
                    sm.send_message(connection, msg)
                    msg = sm.get_response(connection)
                    if msg.text == 'x':
                        self.playerPCsymbol = 'o'
                        self.player_symbol = 'x'
                        break
                    elif msg.text == 'o':
                        self.playerPCsymbol = 'x'
                        self.player_symbol = 'o'
                        break
                    else:
                        msg.text = 'Wrong symbol! Choose again!'
                        msg.type = 1
                        sm.send_message(connection, msg)

                print('-' * 15)
                while self.game:
                    if random.random() < 0.5:
                        self.you_go_first = True
                        msg.type = 10
                        msg.text = 'You go first!'
                    else:
                        self.you_go_first = False
                        msg.type = 10
                        msg.text = 'PC goes first!'
                    sm.send_message(connection, msg)
                    while True:
                        if self.you_go_first:
                            msg.type = 10
                            msg.text = 'Your turn!'
                            sm.send_message(connection, msg)
                            self.board.print_board()
                            msg.tab = self.board.board_to_string()
                            msg.type = 2
                            sm.send_message(connection, msg)
                            while True:
                                msg.type = 3
                                sm.send_message(connection, msg)
                                msg = sm.get_response(connection)
                                if self.board.insert_symbol([msg.x, msg.y], self.player_symbol):
                                    break
                            self.board.print_board()
                            msg.tab = self.board.board_to_string()
                            msg.type = 2
                            sm.send_message(connection, msg)
                            if self.board.win_check(self.player_symbol):
                                msg.text = 'You WIN'
                                msg.type = 10
                                sm.send_message(connection, msg)
                                self.board.print_board()
                                msg.tab = self.board.board_to_string()
                                msg.type = 2
                                sm.send_message(connection, msg)
                                break
                            if self.board.is_board_full():
                                print('Board is full. Nobody won!')
                                msg.text = 'Board is full. Nobody won!'
                                msg.type = 10
                                sm.send_message(connection, msg)
                                self.board.print_board()
                                msg.tab = self.board.board_to_string()
                                msg.type = 2
                                sm.send_message(connection, msg)
                                break

                            while True:
                                if self.board.insert_symbol([random.randint(0, 2), random.randint(0, 2)], self.playerPCsymbol):
                                    break
                            if self.board.win_check(self.playerPCsymbol):
                                msg.text = 'HAHA You LOOSE!'
                                msg.type = 10
                                sm.send_message(connection, msg)
                                self.board.print_board()
                                msg.tab = self.board.board_to_string()
                                msg.type = 2
                                sm.send_message(connection, msg)
                                break
                            if self.board.is_board_full():
                                msg.text = 'Board is full. Nobody won!'
                                msg.type = 10
                                sm.send_message(connection, msg)
                                print('Board is full. Nobody won!')
                                self.board.print_board()
                                msg.tab = self.board.board_to_string()
                                msg.type = 2
                                sm.send_message(connection, msg)
                                break
                        else:
                            while True:
                                if self.board.insert_symbol([random.randint(0, 2), random.randint(0, 2)],
                                                            self.playerPCsymbol):
                                    break
                            if self.board.win_check(self.playerPCsymbol):
                                msg.text = 'HAHA You LOOSE!'
                                msg.type = 10
                                sm.send_message(connection, msg)
                                self.board.print_board()
                                msg.tab = self.board.board_to_string()
                                msg.type = 2
                                sm.send_message(connection, msg)
                                break
                            if self.board.is_board_full():
                                msg.text = 'Board is full. Nobody won!'
                                msg.type = 10
                                sm.send_message(connection, msg)
                                print('Board is full. Nobody won!')
                                self.board.print_board()
                                msg.tab = self.board.board_to_string()
                                msg.type = 2
                                sm.send_message(connection, msg)
                                break

                            msg.type = 10
                            msg.text = 'Your turn!'
                            sm.send_message(connection, msg)
                            self.board.print_board()
                            msg.tab = self.board.board_to_string()
                            msg.type = 2
                            sm.send_message(connection, msg)
                            while True:
                                msg.type = 3
                                sm.send_message(connection, msg)
                                msg = sm.get_response(connection)
                                if self.board.insert_symbol([msg.x, msg.y], self.player_symbol):
                                    break
                            self.board.print_board()
                            msg.tab = self.board.board_to_string()
                            msg.type = 2
                            sm.send_message(connection, msg)
                            if self.board.win_check(self.player_symbol):
                                msg.text = 'You WIN'
                                msg.type = 10
                                sm.send_message(connection, msg)
                                self.board.print_board()
                                msg.tab = self.board.board_to_string()
                                msg.type = 2
                                sm.send_message(connection, msg)
                                break
                            if self.board.is_board_full():
                                print('Board is full. Nobody won!')
                                msg.text = 'Board is full. Nobody won!'
                                msg.type = 10
                                sm.send_message(connection, msg)
                                self.board.print_board()
                                msg.tab = self.board.board_to_string()
                                msg.type = 2
                                sm.send_message(connection, msg)
                                break
            else:
                number = random.randint(0, 100)
                print(number)
                while 1:
                    msg = protoc_pb2.msg()
                    msg.type = 4
                    sm.send_message(connection, msg)
                    msg = sm.get_response(connection)
                    msg.type = 10
                    if msg.guess == number:
                        msg.text = 'guessed it'
                        sm.send_message(connection, msg)
                        break
                    elif msg.guess > number:
                        msg.text = 'less'
                    elif msg.guess < number:
                        msg.text = 'more'
                    sm.send_message(connection, msg)


if __name__ == '__main__':
    game = TicTacToeGame()
    game.start_game()
