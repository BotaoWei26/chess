from Piece import *
from functools import reduce


class Rook(Piece):
    def __init__(self, row, col, color):
        Piece.__init__(self, row, col, color, 'r')

    def green_moves(self, pieces):
        moves = []
        for i in range(8):
            moves.append([self.row, i])
            moves.append([i, self.col])



    def red_moves(self, pieces):
        return []
        """
        moves = []
        if self.color == "b":
            moves.append([self.row + 1, self.col - 1])
            moves.append([self.row + 1, self.col + 1])
        elif self.color == "w":
            moves.append([self.row - 1, self.col - 1])
            moves.append([self.row - 1, self.col + 1])
        return list(filter(lambda x: detect_collision(x, pieces, self.color), moves))
        """
