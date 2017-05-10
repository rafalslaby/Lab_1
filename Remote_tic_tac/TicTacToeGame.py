from Board import Board
import random
import socket
import socket_management as sm
import protoc_pb2


def send_text(connection, msg, text):
    msg.type = 10
    msg.text = text
    sm.send_message(connection, msg)


def send_tab(connection, msg, tab):
    msg.tab = tab
    msg.type = 2
    sm.send_message(connection, msg)


def event_handler(connection, msg, tab, win_lose_full):
    send_tab(connection, msg, tab)
    if win_lose_full == 1:
        msg.text = '-' * 8 + '\nYou WIN\n' + '-' * 8
    elif win_lose_full == 2:
        msg.text = '-' * 8 + '\nHAHA you LOSE!\n' + '-' * 8
    else:
        msg.text = '-' * 8 + '\nBoard is full. Nobody won!\n' + '-' * 8
    msg.type = 10
    sm.send_message(connection, msg)


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
                return
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
                        send_text(connection, msg, 'You go first!')
                    else:
                        self.you_go_first = False
                        send_text(connection, msg, 'PC goes first!')
                    while True:
                        if self.you_go_first:
                            send_text(connection, msg, 'Your turn!')
                            self.board.print_board()
                            send_tab(connection, msg, self.board.board_to_string())
                            while True:
                                msg.type = 3
                                sm.send_message(connection, msg)
                                msg = sm.get_response(connection)
                                if self.board.insert_symbol([msg.x, msg.y], self.player_symbol):
                                    break
                            self.board.print_board()
                            # msg.tab = self.board.board_to_string()
                            # msg.type = 2
                            # sm.send_message(connection, msg)
                            if self.board.win_check(self.player_symbol):
                                event_handler(connection, msg, self.board.board_to_string(), 1)
                                self.board.print_board()
                                break
                            if self.board.is_board_full():
                                event_handler(connection, msg, self.board.board_to_string(), 3)
                                self.board.print_board()
                                break

                            while True:
                                if self.board.insert_symbol([random.randint(0, 2), random.randint(0, 2)], self.playerPCsymbol):
                                    break
                            if self.board.win_check(self.playerPCsymbol):
                                event_handler(connection, msg, self.board.board_to_string(), 2)
                                self.board.print_board()
                                break
                            if self.board.is_board_full():
                                event_handler(connection, msg, self.board.board_to_string(), 3)
                                self.board.print_board()
                                break
                        else:
                            while True:
                                if self.board.insert_symbol([random.randint(0, 2), random.randint(0, 2)],
                                                            self.playerPCsymbol):
                                    break
                            if self.board.win_check(self.playerPCsymbol):
                                event_handler(connection, msg, self.board.board_to_string(), 2)
                                self.board.print_board()
                                break
                            if self.board.is_board_full():
                                event_handler(connection, msg, self.board.board_to_string(), 3)
                                self.board.print_board()
                                break

                            send_text(connection, msg, 'Your turn!')
                            self.board.print_board()
                            send_tab(connection, msg, self.board.board_to_string())
                            while True:
                                msg.type = 3
                                sm.send_message(connection, msg)
                                msg = sm.get_response(connection)
                                if self.board.insert_symbol([msg.x, msg.y], self.player_symbol):
                                    break
                            self.board.print_board()
                            # msg.tab = self.board.board_to_string()
                            # msg.type = 2
                            # sm.send_message(connection, msg)
                            if self.board.win_check(self.player_symbol):
                                event_handler(connection, msg, self.board.board_to_string(), 1)
                                self.board.print_board()
                                break
                            if self.board.is_board_full():
                                event_handler(connection, msg, self.board.board_to_string(), 3)
                                self.board.print_board()
                                break
                    self.board.clean_board()
                    break
            else:
                msg = protoc_pb2.msg()
                msg.type = 4
                sm.send_message(connection, msg)
                msg = sm.get_response(connection)
                if msg.x > msg.y:
                    send_text(connection, msg, 'x > y')
                    break
                number = random.randint(msg.x, msg.y)
                print(number)
                while 1:
                    msg.type = 5
                    sm.send_message(connection, msg)
                    msg = sm.get_response(connection)
                    msg.type = 10
                    if msg.guess == number:
                        msg.text = '-' * 8 + 'You guessed it' + '-' * 8
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
