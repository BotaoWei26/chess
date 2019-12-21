class Piece:
    def __init__(self, row, col, color, piece_type):
        self.row = row
        self.col = col
        self.color = color
        self.piece_type = piece_type

    def move(self, row, col):
        self.row = row
        self.col = col

def detect_collision(move, pieces):
    if not ((0 <= move[0] <= 7) or  0 <= move[1] <= 7):
        return False
    for piece in pieces:
        if [move[0], move[1]] == [piece.row, piece.col]:
            return False
    return True
