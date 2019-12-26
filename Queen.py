from Piece import *


class Queen(Piece):
    def __init__(self, row, col, color):
        Piece.__init__(self, row, col, color, 'q')

    def green_moves(self, pieces):
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
        #up_right
        counter = 1
        while True:
            move = [self.row - counter, self.col + counter]
            if (not detect_off(move)) and not (detect_collision(move, pieces)):
                moves.append(move)
                counter += 1
            else:
                break
        #right_down
        counter = 1
        while True:
            move = [self.row + counter, self.col + counter]
            if (not detect_off(move)) and not (detect_collision(move, pieces)):
                moves.append(move)
                counter += 1
            else:
                break
        #down_left
        counter = 1
        while True:
            move = [self.row + counter, self.col - counter]
            if (not detect_off(move)) and not (detect_collision(move, pieces)):
                moves.append(move)
                counter += 1
            else:
                break
        #left_up
        counter = 1
        while True:
            move = [self.row - counter, self.col - counter]
            if (not detect_off(move)) and not (detect_collision(move, pieces)):
                moves.append(move)
                counter += 1
            else:
                break
        return moves

    def red_moves(self, pieces):
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
        #up_right
        counter = 1
        while True:
            move = [self.row - counter, self.col + counter]
            if detect_collision(move, pieces, self.color):
                moves.append(move)
                break
            elif detect_off(move) or detect_collision(move, pieces):
                break
            else:
                counter += 1
        #right_down
        counter = 1
        while True:
            move = [self.row + counter, self.col + counter]
            if detect_collision(move, pieces, self.color):
                moves.append(move)
                break
            elif detect_off(move) or detect_collision(move, pieces):
                break
            else:
                counter += 1
        #down_left
        counter = 1
        while True:
            move = [self.row + counter, self.col - counter]
            if detect_collision(move, pieces, self.color):
                moves.append(move)
                break
            elif detect_off(move) or detect_collision(move, pieces):
                break
            else:
                counter += 1
        #left_up
        counter = 1
        while True:
            move = [self.row - counter, self.col - counter]
            if detect_collision(move, pieces, self.color):
                moves.append(move)
                break
            elif detect_off(move) or detect_collision(move, pieces):
                break
            else:
                counter += 1
        return moves

    def special_moves(self, pieces):
        return [[None]]