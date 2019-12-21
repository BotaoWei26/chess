from Piece import *


class Bishop(Piece):
    def __init__(self, row, col, color):
        Piece.__init__(self, row, col, color, 'b')