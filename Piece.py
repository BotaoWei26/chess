from copy import deepcopy


class Piece:
    def __init__(self, row, col, color, piece_type):
        self.row = row
        self.col = col
        self.color = color
        self.piece_type = piece_type
        self.passable = False
        self.first_move = True

    def move(self, row, col):
        self.row = row
        self.col = col
        self.first_move = False

    def reset(self):
        self.passable = False

    def check_check(self, pieces):
        return False


