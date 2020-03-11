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

    def direction_function(self, direction):
        if direction == "up":
            return lambda c: [self.row - c, self.col]
        elif direction == "right":
            return lambda c: [self.row, self.col + c]
        elif direction == "down":
            return lambda c: [self.row + c, self.col]
        elif direction == "left":
            return lambda c: [self.row, self.col - c]

        elif direction == "up_right":
            return lambda c: [self.row - c, self.col + c]
        elif direction == "right_down":
            return lambda c: [self.row + c, self.col + c]
        elif direction == "down_left":
            return lambda c: [self.row + c, self.col - c]
        elif direction == "left_up":
            return lambda c: [self.row - c, self.col - c]
