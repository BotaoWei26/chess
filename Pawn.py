from Piece import *


class Pawn(Piece):
    def __init__(self, row, col, color):
        Piece.__init__(self, row, col, color, 'p')

    def green_moves(self, pieces):
        moves = []
        if self.color == "b":
            moves.append([self.row + 1, self.col])
            if self.row == 1:
                moves.append([self.row + 2, self.col])
        elif self.color == "w":
            moves.append([self.row - 1, self.col])
            if self.row == 6:
                moves.append([self.row - 2, self.col])

        return list(filter(lambda x: detect_collision(x, pieces), moves))
