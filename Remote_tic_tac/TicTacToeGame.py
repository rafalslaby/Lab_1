from Board import Board
from Player import Player
import random
import time
import socket


class TicTacToeGame:
    def __init__(self):
        self.board = Board()
        self.player = Player()
        self.game = True
        self.you_go_first = True

    def start_game(self):
        host = 'localhost'
        port = 50001
        data_size = 1024
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (host, port)
        sock.bind(server_address)
        sock.listen(1)
        connection, client_address = sock.accept()

        print('-'*15)
        while True:
            self.player.symbol = str(input('Choose your symbol: x or o  '))
            if self.player.symbol == 'x':
                self.playerPCsymbol = 'o'
                break
            elif self.player.symbol == 'o':
                self.playerPCsymbol = 'x'
                break
            else:
                print('Wrong symbol! Choose again!')

        while self.game:
            print('-'*15)
            print('GAME VERSUS PC STARTS')
            print('-'*15)
            if random.random() < 0.5:
                self.you_go_first = True
                print('You go first!')
            else:
                self.you_go_first = False
                print('PC goes firs!')

            while True:
                if self.you_go_first:
                    print('Your turn!')
                    self.board.print_board()
                    while True:
                        if self.board.insert_symbol(self.player.get_player_move(), self.player.symbol):
                            break
                    self.board.print_board()
                    if self.board.win_check(self.player.symbol):
                        print('You WIN!')
                        break
                    if self.board.is_board_full():
                        print('Board is full. Nobody won!')
                        break
                    print('PCs turn!')
                    time.sleep(1.5)
                    x = []
                    while True:
                        if len(x) == 0:
                            connection.send(b'1')
                        else:
                            connection.send(b'2')
                        data = connection.recv(data_size)
                        if data:
                            x.append(int(bytes.decode(data, encoding='utf-8')))
                            if len(x) == 2:
                                if self.board.insert_symbol(x, self.playerPCsymbol):
                                    break
                                x = []
                    self.board.print_board()
                    if self.board.win_check(self.playerPCsymbol):
                        print('HAHA You LOOSE!')
                        break
                    if self.board.is_board_full():
                        print('Board is full. Nobody won!')
                        break
                else:
                    print('PCs turn')
                    time.sleep(1.5)
                    x = []
                    while True:
                        if len(x) == 0:
                            connection.send(b'1')
                        else:
                            connection.send(b'2')
                        data = connection.recv(data_size)
                        if data:
                            x.append(int(bytes.decode(data, encoding='utf-8')))
                            if len(x) == 2:
                                if self.board.insert_symbol(x, self.playerPCsymbol):
                                    break
                                x = []
                    self.board.print_board()
                    if self.board.win_check(self.playerPCsymbol):
                        print('HAHA You LOOSE!')
                        break
                    if self.board.is_board_full():
                        print('Board is full. Nobody won!')
                        break

                    print('Your turn')
                    while True:
                        if self.board.insert_symbol(self.player.get_player_move(), self.player.symbol):
                            break
                    self.board.print_board()
                    if self.board.win_check(self.player.symbol):
                        print('You WIN!')
                        break
                    if self.board.is_board_full():
                        print('Board is full. Nobody won!')
                        break

            if input('Wanna play again? (y/n)') == 'n':
                self.game = False
                print('Hope you had fun')
            else:
                self.board.clean_board()

if __name__ == '__main__':
    game = TicTacToeGame()
    game.start_game()
