from Piece import *
from boardFunctions import *



class Rook(Piece):
    def __init__(self, row, col, color):
        Piece.__init__(self, row, col, color, 'r')
        self.directions = ["up", "right", "down", "left"]

    def green_moves(self, pieces, real=False):
        moves = []

        #checks all directions
        for direction in self.directions:
            counter = 1
            position_function = self.direction_function(direction)
            move = position_function(counter)
            while (not detect_off(move)) and not (detect_collision(move, pieces)): # not off board and not on another piece
                moves.append(move)
                counter += 1
                move = position_function(counter)
        #stops recursive loop in check?
        if real:
            moves = list(filter(lambda x: not check_check_all(pieces, self.color, x, self), moves))

        return moves

    def red_moves(self, pieces, real=False):
        moves = []

        #checks all directions
        for direction in self.directions:
            counter = 1
            position_function = self.direction_function(direction)
            move = position_function(counter)
            while True:
                if detect_collision(move, pieces, self.color):
                    moves.append(move)
                    break
                elif detect_off(move) or detect_collision(move, pieces):
                    break
                counter += 1
                move = position_function(counter)

        if real:
            moves = list(filter(lambda x: not check_check_all(pieces, self.color, x, self, x), moves))
        return moves

    def special_moves(self, pieces, real=False):
        return []
