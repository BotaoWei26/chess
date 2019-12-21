from Piece import *


class Pawn(Piece):
    def __init__(self, row, col, color):
        Piece.__init__(self, row, col, color, 'p')