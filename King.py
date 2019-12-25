from Piece import *


class King(Piece):
    def __init__(self, row, col, color):
        Piece.__init__(self, row, col, color, 'k')

    def green_moves(self, pieces):
        moves = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if not (i == 0 and j == 0):
                    moves.append([self.row + i, self.col + j])
        return list(filter(lambda x: not detect_collision(x, pieces) and not detect_off(x), moves))

    def red_moves(self, pieces):
        moves = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if not (i == 0 and j == 0):
                    moves.append([self.row + i, self.col + j])
        return list(filter(lambda x: detect_collision(x, pieces, self.color), moves))
