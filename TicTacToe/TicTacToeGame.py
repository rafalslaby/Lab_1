from PC import PC
from Board import Board
from Player import Player
import random
import time


class TicTacToeGame:
    def __init__(self):
        self.board = Board()
        self.player = Player()
        self.playerPC = PC(self.board.board_size)
        self.game = True
        self.you_go_first = True

    def start_game(self):
        print('-'*15)
        while True:
            self.player.symbol = str(input('Choose your symbol: x or o'))
            if self.player.symbol == 'x':
                self.playerPC.symbol = 'o'
                break
            elif self.player.symbol == 'o':
                self.playerPC.symbol = 'x'
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
                    time.sleep(2)
                    while True:
                        if self.board.insert_symbol(self.playerPC.get_PC_move(), self.playerPC.symbol):
                            break
                    self.board.print_board()
                    if self.board.win_check(self.playerPC.symbol):
                        print('HAHA You LOOSE!')
                        break
                    if self.board.is_board_full():
                        print('Board is full. Nobody won!')
                        break
                else:
                    print('PCs turn')
                    time.sleep(2)
                    while True:
                        if self.board.insert_symbol(self.playerPC.get_PC_move(), self.playerPC.symbol):
                            break
                    self.board.print_board()
                    if self.board.win_check(self.playerPC.symbol):
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
