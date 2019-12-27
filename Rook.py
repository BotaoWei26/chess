from Piece import *
from boardFunctions import *



class Rook(Piece):
    def __init__(self, row, col, color):
        Piece.__init__(self, row, col, color, 'r')

    def green_moves(self, pieces, real=False):
        moves = []
        #up
        counter = 1
        while True:
            move = [self.row - counter, self.col]
            if (not detect_off(move)) and not (detect_collision(move, pieces)):
                moves.append(move)
                counter += 1
            else:
                break
        #right
        counter = 1
        while True:
            move = [self.row, self.col + counter]
            if (not detect_off(move)) and not (detect_collision(move, pieces)):
                moves.append(move)
                counter += 1
            else:
                break
        #down
        counter = 1
        while True:
            move = [self.row + counter, self.col]
            if (not detect_off(move)) and not (detect_collision(move, pieces)):
                moves.append(move)
                counter += 1
            else:
                break
        #left
        counter = 1
        while True:
            move = [self.row, self.col - counter]
            if (not detect_off(move)) and not (detect_collision(move, pieces)):
                moves.append(move)
                counter += 1
            else:
                break

        if real:
            moves = list(filter(lambda x: not check_check_all(pieces, self.color, x, self), moves))
        return moves

    def red_moves(self, pieces, real=False):
        moves = []
        #up
        counter = 1
        while True:
            move = [self.row - counter, self.col]
            if detect_collision(move, pieces, self.color):
                moves.append(move)
                break
            elif detect_off(move) or detect_collision(move, pieces):
                break
            else:
                counter += 1
        #right
        counter = 1
        while True:
            move = [self.row, self.col + counter]
            if detect_collision(move, pieces, self.color):
                moves.append(move)
                break
            elif detect_off(move) or detect_collision(move, pieces):
                break
            else:
                counter += 1
        #down
        counter = 1
        while True:
            move = [self.row + counter, self.col]
            if detect_collision(move, pieces, self.color):
                moves.append(move)
                break
            elif detect_off(move) or detect_collision(move, pieces):
                break
            else:
                counter += 1
        #left
        counter = 1
        while True:
            move = [self.row, self.col - counter]
            if detect_collision(move, pieces, self.color):
                moves.append(move)
                break
            elif detect_off(move) or detect_collision(move, pieces):
                break
            else:
                counter += 1

        if real:
            moves = list(filter(lambda x: not check_check_all(pieces, self.color, x, self, x), moves))
        return moves

    def special_moves(self, pieces, real=False):
        return []
