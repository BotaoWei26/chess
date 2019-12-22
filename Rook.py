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
        moves = list(filter(lambda x: x != [self.row, self.col], moves))
        moves = list(filter(lambda x: not detect_collision(x, pieces), moves))
        moves = list(filter(lambda x: (not detect_block(x, [self.row, self.col], pieces, True, False)) and
                                      (not detect_block(x, [self.row, self.col], pieces, False, True)), moves))
        return moves

    def red_moves(self, pieces):
        moves = []
        for i in range(8):
            moves.append([self.row, i])
            moves.append([i, self.col])
        moves = list(filter(lambda x: x != [self.row, self.col], moves))
        moves = list(filter(lambda x: detect_collision(x, pieces, self.color), moves))
        moves = list(filter(lambda x: (not detect_block(x, [self.row, self.col], pieces, True, False)) and
                                      (not detect_block(x, [self.row, self.col], pieces, False, True)), moves))
        return moves
