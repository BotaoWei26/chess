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

        self.turn = 'w'
        self.current_piece = None
        self.green_moves = []

    def toggle_turn(self):
        if self.turn == 'b':
            self.turn = 'w'
        elif self.turn == 'w':
            self.turn = 'b'

    def pick(self, row, col):
        self.current_piece = None
        for piece in self.pieces:
            if ([piece.row, piece.col] == [row, col]) and (piece.color == self.turn):
                self.current_piece = piece
                self.green_moves = piece.green_moves(self.pieces)
                break
        return self.current_piece is not None

    def move(self, row, col):
        if [row, col] in self.green_moves:
            self.current_piece.move(row, col)
            self.toggle_turn()
            self.current_piece = None
            self.green_moves = []
            return True
        return False
