from Piece import *


class Rook(Piece):
    def __init__(self, row, col, color):
        Piece.__init__(self, row, col, color, 'r')