from Piece import *


class King(Piece):
    def __init__(self, row, col, color):
        Piece.__init__(self, row, col, color, 'k')

    def green_moves(self, pieces):
        moves = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if not (i == 0 and j == 0):
                    moves.append([self.row + i, self.col + j])
        return list(filter(lambda x: not detect_collision(x, pieces) and not detect_off(x), moves))

    def red_moves(self, pieces):
        moves = []
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if not (i == 0 and j == 0):
                    moves.append([self.row + i, self.col + j])
        return list(filter(lambda x: detect_collision(x, pieces, self.color), moves))

    def special_moves(self, pieces):
        moves = [[None]]
        if self.color == 'b' and [self.row, self.col] == [0, 4] and self.first_move:
            for piece in pieces:
                if [piece.row, piece.col] == [0, 0] and piece.first_move:
                    block = False
                    for piece_block in pieces:
                        pb = [piece_block.row, piece_block.col]
                        if pb == [0, 1] or pb == [0, 2] or pb == [0, 3]:
                            block = True
                    if not block:
                        moves.append(["castling", [0, 2], [0, 3], [piece.row, piece.col]])
                elif [piece.row, piece.col] == [0, 7] and piece.first_move:
                    block = False
                    for piece_block in pieces:
                        pb = [piece_block.row, piece_block.col]
                        if pb == [0, 5] or pb == [0, 6]:
                            block = True
                    if not block:
                        moves.append(["castling", [0, 6], [0, 5], [piece.row, piece.col]])

        if self.color == 'w' and [self.row, self.col] == [7, 4] and self.first_move:
            for piece in pieces:
                if [piece.row, piece.col] == [7, 0] and piece.first_move:
                    block = False
                    for piece_block in pieces:
                        pb = [piece_block.row, piece_block.col]
                        if pb == [7, 1] or pb == [7, 2] or pb == [7, 3]:
                            block = True
                    if not block:
                        moves.append(["castling", [7, 2], [7, 3], [piece.row, piece.col]])
                elif [piece.row, piece.col] == [7, 7] and piece.first_move:
                    block = False
                    for piece_block in pieces:
                        pb = [piece_block.row, piece_block.col]
                        if pb == [7, 5] or pb == [7, 6]:
                            block = True
                    if not block:
                        moves.append(["castling", [7, 6], [7, 5], [piece.row, piece.col]])
        return moves