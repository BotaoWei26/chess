class Piece:
    def __init__(self, row, col, color, piece_type):
        self.row = row
        self.col = col
        self.color = color
        self.piece_type = piece_type

    def move(self, row, col):
        self.row = row
        self.col = col


def detect_collision(move, pieces, color="none"):
    for piece in pieces:
        if [move[0], move[1]] == [piece.row, piece.col]:
            if (color == 'b' and piece.color == 'w') or \
               (color == 'w' and piece.color == 'b') or \
               (color == "none"):
                return True
    return False


def detect_off(move):
    return not (0 <= move[0] <= 7) or (0 <= move[1] <= 7)


def detect_block(move, place, pieces, vertical, horizontal):
    for piece in pieces:
        if vertical and horizontal:
            return False
        elif vertical:
            if [piece.row, piece.col] in [[x, place[1]] for x in (list(range(move[0]+1, place[0])) +
                                                                  list(range(place[0]+1, move[0])))]:
                return True
        elif horizontal:
            if [piece.row, piece.col] in [[place[0], x] for x in (list(range(move[1]+1, place[1])) +
                                                                  list(range(place[1]+1, move[1])))]:
                return True
    return False