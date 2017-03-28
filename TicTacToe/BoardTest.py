import unittest
from Board import Board


class TestBoard(unittest.TestCase):
    def test_should_return_false_when_trying_to_fill_filled_place(self):
        test_board = Board()
        test_board.insert_symbol([0, 0], 'x')
        expected_result = False
        self.assertEqual(test_board.insert_symbol([0, 0], 'x'), expected_result)

    def test_should_return_false_when_chosing_wrong_symbol(self):
        test_board = Board()
        symbol = 'K'
        expected_result = False
        self.assertEqual(test_board.insert_symbol([0, 0], symbol), expected_result)

    def test_should_return_false_when_out_of_board(self):
        test_board = Board()
        expected_result = False
        self.assertEqual(test_board.insert_symbol([3, 0], 'x'), expected_result)

    def test_should_return_false_when_coordinates_are_not_of_integer_type(self):
        test_board = Board()
        expected_result = False
        self.assertEqual(test_board.insert_symbol(['a', 1], 'x'), expected_result)
        self.assertEqual(test_board.insert_symbol([1, 'b'], 'x'), expected_result)

    def test_should_return_true_when_board_is_full(self):
        test_board = Board()
        expected_result = True
        for i in range(test_board.board_size):
            for j in range(test_board.board_size):
                test_board.insert_symbol([i, j], 'x')
        self.assertEqual(test_board.is_board_full(), expected_result)

    def test_should_return_true_when_one_of_players_won(self):
        test_board = Board()
        expected_result = True
        for i in range(test_board.board_size):
            test_board.board[1][i] = 'x'
        self.assertEqual(test_board.win_check('x'), expected_result)
        test_board.clean_board()

        for i in range(test_board.board_size):
            test_board.board[i][i] = 'x'
        self.assertEqual(test_board.win_check('x'), expected_result)
        test_board.clean_board()

        for i in range(test_board.board_size):
            test_board.board[i][1] = 'x'
        self.assertEqual(test_board.win_check('x'), expected_result)
        test_board.clean_board()

        for i in range(test_board.board_size):
            test_board.board[i][test_board.board_size - i - 1] = 'x'
        self.assertEqual(test_board.win_check('x'), expected_result)

if __name__ == '__main__':
    unittest.main()
