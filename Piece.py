class Piece:
    def __init__(self, row, col, color, piece_type):
        self.row = row
        self.col = col
        self.color = color
        self.piece_type = piece_type
        self.passable = False
        self.first_move = True

    def move(self, row, col):
        self.row = row
        self.col = col
        self.first_move = False


    def reset(self):
        self.passable = False


def detect_collision(move, pieces, color="none"):
    for piece in pieces:
        if [move[0], move[1]] == [piece.row, piece.col]:
            if (color == 'b' and piece.color == 'w') or \
               (color == 'w' and piece.color == 'b') or \
               (color == "none"):
                return True
    return False


def detect_off(move):
    return not ((0 <= move[0] <= 7) and (0 <= move[1] <= 7))
