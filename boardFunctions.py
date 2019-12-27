from copy import deepcopy


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


def check_check_all(pieces, color, move=[], piece_moved=None, piece_removed=None):
    pieces = deepcopy(pieces)
    if piece_removed is not None:
        pieces = [piece for piece in pieces if [piece.row, piece.col] != piece_removed]
    for piece in pieces:
        if [piece.row, piece.col] == [piece_moved.row, piece_moved.col] and move != []:
            piece.move(move[0], move[1])
    for piece in pieces:
        if piece.check_check(pieces) and color == piece.color:
            return True
    return False
