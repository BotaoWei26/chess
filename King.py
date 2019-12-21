from Piece import *


class King(Piece):
    def __init__(self, row, col, color):
        Piece.__init__(self, row, col, color, 'k')