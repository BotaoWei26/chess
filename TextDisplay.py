class TextDisplay:
    def __init__(self, game):
        self.grid = []
        self.selected = None
        self.game = game
        self.update()

    def update(self):
        self.grid = [['--' for j in range(8)] for i in range(8)]
        for piece in self.game.pieces:
            self.grid[piece.row][piece.col] = piece.color + piece.piece_type

        self.selected = self.game.current_piece
        if self.selected is not None:
            self.grid[self.selected.row][self.selected.col] = self.grid[self.selected.row][self.selected.col].upper()

        for move in self.game.green_moves:
            self.grid[move[0]][move[1]] = '**'

    def display(self):
        for row in self.grid:
            for tile in row:
                print(tile[0] + tile[1] + " ", end=" ")
            print("\n")
