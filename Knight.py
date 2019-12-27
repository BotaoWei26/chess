from Piece import *


class Knight(Piece):
    def __init__(self, row, col, color):
        Piece.__init__(self, row, col, color, 'n')

    def green_moves(self, pieces, real=False):
        moves = []
        for i in [-2, -1, 1, 2]:
            for j in [-2, -1, 1, 2]:
                if (i + j) % 2 != 0:
                    moves.append([self.row + i, self.col + j])
        moves = list(filter(lambda x: not detect_collision(x, pieces) and not detect_off(x), moves))
        if real:
            moves = list(filter(lambda x: not check_check_all(pieces, self.color, x, self), moves))
        return moves

    def red_moves(self, pieces, real=False):
        moves = []
        for i in [-2, -1, 1, 2]:
            for j in [-2, -1, 1, 2]:
                if (i + j) % 2 != 0:
                    moves.append([self.row + i, self.col + j])
        moves = list(filter(lambda x: detect_collision(x, pieces, self.color), moves))
        if real:
            moves = list(filter(lambda x: not check_check_all(pieces, self.color, x, self, x), moves))
        return moves

    def special_moves(self, pieces, real=False):
        return [[None]]
