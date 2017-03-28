import random


class PC:
    def __init__(self, range):
        self.range = range

    def get_PC_move(self):
        return [random.randint(0, self.range-1), random.randint(0, self.range-1)]
