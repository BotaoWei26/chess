class TextDisplay:
    def __init__(self, game):
        self.grid = []
        self.game = game
        self.update()

    def update(self):
        self.grid = [['--' for j in range(8)] for i in range(8)]
        for piece in self.game.pieces:
            self.grid[piece.row][piece.col] = [piece.color, piece.piece_type]

    def display(self):
        for row in self.grid:
            for tile in row:
                print(tile[0] + tile[1] + " ", end=" ")
            print("\n")
