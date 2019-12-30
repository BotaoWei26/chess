from Piece import *
from boardFunctions import *


class King(Piece):
    def __init__(self, row, col, color):
        Piece.__init__(self, row, col, color, 'k')

    def green_moves(self, pieces, real=False):
        moves = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if not (i == 0 and j == 0):
                    moves.append([self.row + i, self.col + j])
        moves = list(filter(lambda x: not detect_collision(x, pieces) and not detect_off(x), moves))
        if real:
            moves = list(filter(lambda x: not check_check_all(pieces, self.color, x, self), moves))
        return moves

    def red_moves(self, pieces, real=False):
        moves = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if not (i == 0 and j == 0):
                    moves.append([self.row + i, self.col + j])
        moves = list(filter(lambda x: detect_collision(x, pieces, self.color), moves))
        if real:
            moves = list(filter(lambda x: not check_check_all(pieces, self.color, x, self, x), moves))
        return moves

    def special_moves(self, pieces, real=False):
        moves = []
        if self.color == 'b' and [self.row, self.col] == [0, 4] and self.first_move:
            for piece in pieces:
                if [piece.row, piece.col] == [0, 0] and piece.first_move and \
                    not detect_collision([0, 1], pieces) and not detect_collision([0, 2], pieces) and \
                    not detect_collision([0, 3], pieces) and \
                    not check_check_all(pieces, self.color, [], self) and \
                    not check_check_all(pieces, self.color, [0, 1], self) and \
                    not check_check_all(pieces, self.color, [0, 2], self) and \
                    not check_check_all(pieces, self.color, [0, 3], self):
                    moves.append(["castling", [0, 2], [0, 3], [piece.row, piece.col]])
                elif [piece.row, piece.col] == [0, 7] and piece.first_move and \
                    not detect_collision([0, 5], pieces) and not detect_collision([0, 6], pieces) and \
                    not check_check_all(pieces, self.color, [], self) and \
                    not check_check_all(pieces, self.color, [0, 5], self) and \
                    not check_check_all(pieces, self.color, [0, 6], self):
                    moves.append(["castling", [0, 6], [0, 5], [piece.row, piece.col]])

        if self.color == 'w' and [self.row, self.col] == [7, 4] and self.first_move:
            for piece in pieces:
                if [piece.row, piece.col] == [7, 0] and piece.first_move and \
                    not detect_collision([7, 1], pieces) and not detect_collision([7, 2], pieces) and \
                    not detect_collision([7, 3], pieces) and \
                    not check_check_all(pieces, self.color, [], self) and \
                    not check_check_all(pieces, self.color, [7, 1], self) and \
                    not check_check_all(pieces, self.color, [7, 2], self) and \
                    not check_check_all(pieces, self.color, [7, 3], self):
                    moves.append(["castling", [7, 2], [7, 3], [piece.row, piece.col]])
                elif [piece.row, piece.col] == [7, 7] and piece.first_move and \
                    not detect_collision([7, 5], pieces) and not detect_collision([7, 6], pieces) and \
                    not check_check_all(pieces, self.color, [], self) and \
                    not check_check_all(pieces, self.color, [7, 5], self) and \
                    not check_check_all(pieces, self.color, [7, 6], self):
                    moves.append(["castling", [7, 6], [7, 5], [piece.row, piece.col]])
        if real:
            moves = list(filter(lambda x: not check_check_all(pieces, self.color, x[1], self), moves))
        return moves

    def check_check(self, pieces):
        red_moves = []
        for piece in pieces:
            if piece.color != self.color:
                red_moves.extend(piece.red_moves(pieces))
        return [self.row, self.col] in red_moves
