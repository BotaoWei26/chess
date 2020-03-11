from Pawn import Pawn
from Rook import Rook
from Knight import Knight
from Bishop import Bishop
from Queen import Queen
from King import King
from boardFunctions import *
from PromotionScreen import PromotionScreen

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
        self.w_king = King(0, 4, 'b')
        self.pieces.append(self.w_king)
        self.b_king = King(7, 4, 'w')
        self.pieces.append(self.b_king)

        self.turn = 'w'
        self.current_piece = None
        self.green_moves = []
        self.red_moves = []
        self.special_moves = [[None]]
        self.turn_type = 'pick'

    def check_game_over(self):
        check = check_check_all(self.pieces, self.turn, [], self.w_king if self.turn == 'w' else self.b_king)
        moves = []
        for piece in filter(lambda x: x.color == self.turn, self.pieces):
            moves.extend(piece.green_moves(self.pieces, True))
            moves.extend(piece.red_moves(self.pieces, True))
            moves.extend(piece.special_moves(self.pieces, True))
        no_moves = len(moves) == 0
        if check and no_moves:
            return "checkmate"
        elif check:
            return "check"
        elif no_moves:
            return "stalemate"
        else:
            return "nothing"

    def reset(self):
        self.current_piece = None
        self.green_moves = []
        self.red_moves = []
        self.special_moves = []
        self.turn_type = 'pick'

    def toggle_turn(self):
        if self.turn == 'b':
            self.turn = 'w'
        elif self.turn == 'w':
            self.turn = 'b'

    def click(self, row, col):
        if self.turn_type == 'pick':
            self.pick(row, col)
        elif self.turn_type == 'move':
            self.move(row, col)

    def pick(self, row, col):
        self.current_piece = None
        for piece in self.pieces:
            if ([piece.row, piece.col] == [row, col]) and (piece.color == self.turn):
                self.current_piece = piece
                self.green_moves = piece.green_moves(self.pieces, True)
                self.red_moves = piece.red_moves(self.pieces, True)
                self.special_moves = piece.special_moves(self.pieces, True)
                break
        if self.current_piece is None:
            self.turn_type = 'pick'
        else:
            self.turn_type = 'move'

    def move(self, row, col):
        if [row, col] in self.green_moves:
            for piece in self.pieces:
                piece.reset()
            self.current_piece.move(row, col)
            self.toggle_turn()

        elif [row, col] in self.red_moves:
            for piece in self.pieces:
                piece.reset()
            self.pieces = [piece for piece in self.pieces if [piece.row, piece.col] != [row, col]]
            self.current_piece.move(row, col)
            self.toggle_turn()

        for move in self.special_moves:
            if move[0] == 'en_passant' and (move[1] == [row, col] or move[2] == [row, col]):
                for piece in self.pieces:
                    piece.reset()
                self.pieces = [piece for piece in self.pieces if [piece.row, piece.col] != move[2]]
                self.current_piece.move(move[1][0], move[1][1])
                self.toggle_turn()
            elif move[0] == 'castling' and (move[1] == [row, col] or move[2] == [row, col]):
                for piece in self.pieces:
                    piece.reset()
                    if piece.row == move[3][0] and piece.col == move[3][1]:
                        piece.move(move[2][0], move[2][1])
                self.current_piece.move(move[1][0], move[1][1])
                self.toggle_turn()
            elif move[0] == 'passed_pawn' and move[1] == [row, col]:
                for piece in self.pieces:
                    piece.reset()
                self.pieces = [piece for piece in self.pieces if ([piece.row, piece.col] != move[1] and [piece.row, piece.col] != move[2])]

                """ps = PromotionScreen()
                if ps.get() == "queen":
                    self.pieces.append(Queen(move[1][0], move[1][1], self.turn))
                elif ps.get() == "knight":
                    self.pieces.append(Knight(move[1][0], move[1][1], self.turn))
                elif ps.get() == "rook":
                    self.pieces.append(Rook(move[1][0], move[1][1], self.turn))
                elif ps.get() == "bishop":
                    self.pieces.append(Bishop(move[1][0], move[1][1], self.turn))"""
                self.pieces.append(Queen(move[1][0], move[1][1], self.turn))
                self.toggle_turn()
        self.reset()
