from Pawn import *
from Rook import *
from Knight import *
from Bishop import *
from Queen import *
from King import *

class Game:
    def __init__(self):
        self.pieces = []

        for col in range(8):
            self.pieces.append(Pawn(1, col, 'b'))
            self.pieces.append(Pawn(6, col, 'w'))
        for col in [0, 7]:
            self.pieces.append(Rook(0, col, 'b'))
            self.pieces.append(Rook(7, col, 'w'))
        for col in [1, 6]:
            self.pieces.append(Knight(0, col, 'b'))
            self.pieces.append(Knight(7, col, 'w'))
        for col in [2, 5]:
            self.pieces.append(Bishop(0, col, 'b'))
            self.pieces.append(Bishop(7, col, 'w'))
        self.pieces.append(Queen(0, 3, 'b'))
        self.pieces.append(Queen(7, 3, 'w'))
        self.pieces.append(King(0, 4, 'b'))
        self.pieces.append(King(7, 4, 'w'))
