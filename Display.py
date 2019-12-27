from cordDictionary import *

class Display:
    def __init__(self, game):
        self.grid = []
        self.board_colors = [["white" for j in range(8)] for i in range(8)]
        self.selected = None
        self.game = game
        self.update()

    def update(self):
        self.grid = [['--' for j in range(8)] for i in range(8)]
        for piece in self.game.pieces:
            self.grid[piece.row][piece.col] = piece.color + piece.piece_type

        white = True
        for i in range(8):
            for j in range(8):
                self.board_colors[i][j] = "peach puff" if white else "saddle brown"
                white = not white
            white = not white

        for move in self.game.green_moves:
            self.board_colors[move[0]][move[1]] = 'spring green'

        for move in self.game.red_moves:
            self.board_colors[move[0]][move[1]] = 'orange red'

        self.selected = self.game.current_piece
        if self.selected is not None:
            self.board_colors[self.selected.row][self.selected.col] = 'lawn green'

        for move in self.game.special_moves:
            if move[0] == "en_passant":
                self.board_colors[move[1][0]][move[1][1]] = 'OliveDrab3'
                self.board_colors[move[2][0]][move[2][1]] = 'firebrick3'
            if move[0] == "castling":
                self.board_colors[move[1][0]][move[1][1]] = 'coral'
                self.board_colors[move[2][0]][move[2][1]] = 'yellow2'

    def pieces(self):
        return self.grid

    def get_colors(self):
        return self.board_colors