from Piece import *


class Knight(Piece):
    def __init__(self, row, col, color):
        Piece.__init__(self, row, col, color, 'n')