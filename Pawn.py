from Piece import *
from boardFunctions import *


class Pawn(Piece):
    def __init__(self, row, col, color):
        Piece.__init__(self, row, col, color, 'p')

    def move(self, row, col):
        if (self.color == "b" and self.row == 1 and row == 3) or \
           (self.color == "w" and self.row == 6 and row == 4):
            self.passable = True
        Piece.move(self, row, col)

    def green_moves(self, pieces, real=False):
        moves = []
        if self.color == "b" and self.row != 6:
            moves.append([self.row + 1, self.col])
            if self.row == 1 and not detect_collision([self.row + 1, self.col], pieces):
                moves.append([self.row + 2, self.col])
        elif self.color == "w" and self.row != 1:
            moves.append([self.row - 1, self.col])
            if self.row == 6 and not detect_collision([self.row - 1, self.col], pieces):
                moves.append([self.row - 2, self.col])
        moves = list(filter(lambda x: not detect_collision(x, pieces) and not detect_off(x), moves))
        if real:
            moves = list(filter(lambda x: not check_check_all(pieces, self.color, x, self), moves))
        return moves

    def red_moves(self, pieces, real=False):
        moves = []
        if self.color == "b" and self.row != 6:
            moves.append([self.row + 1, self.col - 1])
            moves.append([self.row + 1, self.col + 1])
        elif self.color == "w" and self.row != 1:
            moves.append([self.row - 1, self.col - 1])
            moves.append([self.row - 1, self.col + 1])
        moves = list(filter(lambda x: detect_collision(x, pieces, self.color), moves))
        if real:
            moves = list(filter(lambda x: not check_check_all(pieces, self.color, x, self, x), moves))
        return moves

    def special_moves(self, pieces, real=False):
        moves = []
        if self.color == 'b' and self.row == 4:
            for piece in pieces:
                if piece.passable and abs(self.col - piece.col) == 1:
                    moves.append(["en_passant", [piece.row+1, piece.col], [piece.row, piece.col]])
        if self.color == 'w' and self.row == 3:
            for piece in pieces:
                if piece.passable and abs(self.col - piece.col) == 1:
                    moves.append(["en_passant", [piece.row-1, piece.col], [piece.row, piece.col]])
        if self.color == 'b' and self.row == 6:
            if not detect_collision([7, self.col], pieces):
                moves.append(["passed_pawn", [7, self.col], [6, self.col]])
            if detect_collision([7, self.col - 1], pieces, self.color):
                moves.append(["passed_pawn", [7, self.col - 1], [6, self.col]])
            if detect_collision([7, self.col + 1], pieces, self.color):
                moves.append(["passed_pawn", [7, self.col + 1], [6, self.col]])
        if self.color == 'w' and self.row == 1:
            if not detect_collision([0, self.col], pieces):
                moves.append(["passed_pawn", [0, self.col], [1, self.col]])
            if detect_collision([0, self.col - 1], pieces, self.color):
                moves.append(["passed_pawn", [0, self.col - 1], [1, self.col]])
            if detect_collision([0, self.col + 1], pieces, self.color):
                moves.append(["passed_pawn", [0, self.col + 1], [1, self.col]])
        if real:
            moves = list(filter(lambda x: not check_check_all(pieces, self.color, x[1], self, x[2]), moves))
        return moves
