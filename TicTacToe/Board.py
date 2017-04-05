class Board:

    def __init__(self):
        self.board_size = 3
        self.counter_of_symbols = 0
        self.board = []
        self.clean_board()

    def print_board(self):
        print('-' * 15)
        for i in self.board:
            print(i)
        print('-'*15)

    def clean_board(self):
        self.board = []
        tmp_list = []
        for i in range(self.board_size):
            tmp_list.append('-')
        for i in range(self.board_size):
            self.board.append(tmp_list[:])

    def insert_symbol(self, coordinates, symbol):
        if not (isinstance(coordinates[0], int) and isinstance(coordinates[1], int)):
            print('Coordinates must be integers')
            return False

        if not (symbol == 'x' or symbol == 'o'):
            print('Wrong Symbol!')
            return False

        if not ((0 <= coordinates[0] < self.board_size) and (0 <= coordinates[1] < self.board_size)):
            print('Out of board!')
            return False

        if self.board[coordinates[0]][coordinates[1]] == '-':
            self.board[coordinates[0]][coordinates[1]] = symbol
            self.counter_of_symbols += 1
            return True
        else:
            print('Choose empty field!')
            return False

    def is_board_full(self):
        if self.counter_of_symbols == self.board_size**2:
            return True
        else:
            return False

    def win_check(self, symbol):
        for j in range(self.board_size):
            for k in range(self.board_size):
                if self.board[j][k] != symbol:
                    break
            else:
                return True

        for j in range(self.board_size):
            for k in range(self.board_size):
                if self.board[k][j] != symbol:
                    break
            else:
                return True

        for j in range(self.board_size):
            if self.board[j][j] != symbol:
                break
        else:
            return True

        for j in range(self.board_size):
            if self.board[j][self.board_size - j - 1] != symbol:
                break
        else:
            return True

        return False




