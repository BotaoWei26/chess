from Piece import *


class Knight(Piece):
    def __init__(self, row, col, color):
        Piece.__init__(self, row, col, color, 'n')

    def green_moves(self, pieces):
        moves = []
        for i in [-2, -1, 1, 2]:
            for j in [-2, -1, 1, 2]:
                if (i + j) % 2 != 0:
                    moves.append([self.row + i, self.col + j])
        return list(filter(lambda x: not detect_collision(x, pieces) and not detect_off(x), moves))

    def red_moves(self, pieces):
        moves = []
        for i in [-2, -1, 1, 2]:
            for j in [-2, -1, 1, 2]:
                if (i + j) % 2 != 0:
                    moves.append([self.row + i, self.col + j])
        return list(filter(lambda x: detect_collision(x, pieces, self.color), moves))

    def special_moves(self, pieces):
        return [[None]]