from Piece import *


class Queen(Piece):
    def __init__(self, row, col, color):
        Piece.__init__(self, row, col, color, 'q')