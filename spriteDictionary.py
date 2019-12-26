b_sprite_dict = {
    "p": "sprites/b_pawn.gif",
    "r": "sprites/b_rook.gif",
    "b": "sprites/b_bishop.gif",
    "n": "sprites/b_knight.gif",
    "q": "sprites/b_queen.gif",
    "k": "sprites/b_king.gif"
}
w_sprite_dict = {
    "p": "sprites/w_pawn.gif",
    "r": "sprites/w_rook.gif",
    "b": "sprites/w_bishop.gif",
    "n": "sprites/w_knight.gif",
    "q": "sprites/w_queen.gif",
    "k": "sprites/w_king.gif"
}

def piece_sprite(color, type):
    if color == "w":
        return w_sprite_dict[type]
    elif color == "b":
        return b_sprite_dict[type]
    return ""
