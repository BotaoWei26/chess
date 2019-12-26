from Piece import *


class Pawn(Piece):
    def __init__(self, row, col, color):
        Piece.__init__(self, row, col, color, 'p')

    def move(self, row, col):
        if (self.color == "b" and self.row == 1 and row == 3) or \
           (self.color == "w" and self.row == 6 and row == 4):
            self.passable = True
        Piece.move(self, row, col)

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
        return list(filter(lambda x: not detect_collision(x, pieces) and not detect_off(x), moves))

    def red_moves(self, pieces):
        moves = []
        if self.color == "b":
            moves.append([self.row + 1, self.col - 1])
            moves.append([self.row + 1, self.col + 1])
        elif self.color == "w":
            moves.append([self.row - 1, self.col - 1])
            moves.append([self.row - 1, self.col + 1])
        return list(filter(lambda x: detect_collision(x, pieces, self.color), moves))

    def special_moves(self, pieces):
        moves = [[None]]
        if self.color == 'b' and self.row == 4:
            for piece in pieces:
                if piece.passable:
                    moves.append(["en_passant", [piece.row+1, piece.col], [piece.row, piece.col]])
        if self.color == 'w' and self.row == 3:
            for piece in pieces:
                if piece.passable:
                    moves.append(["en_passant", [piece.row-1, piece.col], [piece.row, piece.col]])
        return moves
