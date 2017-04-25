import Exceptions
import abc


class AbstractTicTacValidator(object):
    __metaclass__ = abc.ABCMeta


class TicTacValidator(AbstractTicTacValidator):
    def validate(coordinate_x, coordinate_y, symbol, board_size):
        #if not (symbol == 'X' or symbol == "O"):
            #raise Exceptions.BadSymbol()
        if not isinstance(coordinate_x, int) and isinstance(coordinate_y, int):
            raise Exceptions.NotInteger()
