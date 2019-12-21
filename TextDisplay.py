from cordDictionary import *

class TextDisplay:
    def __init__(self, game):
        self.grid = []
        self.selected = None
        self.game = game
        self.update()
        self.display()

    def update(self):
        self.grid = [['--' for j in range(8)] for i in range(8)]
        for piece in self.game.pieces:
            self.grid[piece.row][piece.col] = piece.color + piece.piece_type

        self.selected = self.game.current_piece
        if self.selected is not None:
            self.grid[self.selected.row][self.selected.col] = self.grid[self.selected.row][self.selected.col].upper()

        for move in self.game.green_moves:
            self.grid[move[0]][move[1]] = '**'

        for move in self.game.red_moves:
            self.grid[move[0]][move[1]] = '##'

    def display(self):
        print("  ", end=" ")
        for i in cord_col:
            print(i + "  ", end=" ")
        print()

        for row in range(8):
            print(str(8-row) + " ", end=" ")
            for col in range(8):
                print(self.grid[row][col][0] + self.grid[row][col][1] + " ", end=" ")
            print(str(8-row) + " ", end=" ")
            print("\n")

        print("  ", end=" ")
        for i in cord_col:
            print(i + "  ", end=" ")
        print()

