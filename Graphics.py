from tkinter import *
from Game import *
from Display import *


class Graphics:
    def __init__(self):

        self.ts = 64
        self.window = Tk()
        self.game = Game()
        self.display = Display(self.game)

        self.b_sprite_dict = {
            "p": PhotoImage(file="sprites/b_pawn.gif"),
            "r": PhotoImage(file="sprites/b_rook.gif"),
            "b": PhotoImage(file="sprites/b_bishop.gif"),
            "n": PhotoImage(file="sprites/b_knight.gif"),
            "q": PhotoImage(file="sprites/b_queen.gif"),
            "k": PhotoImage(file="sprites/b_king.gif")
        }
        self.w_sprite_dict = {
            "p": PhotoImage(file="sprites/w_pawn.gif"),
            "r": PhotoImage(file="sprites/w_rook.gif"),
            "b": PhotoImage(file="sprites/w_bishop.gif"),
            "n": PhotoImage(file="sprites/w_knight.gif"),
            "q": PhotoImage(file="sprites/w_queen.gif"),
            "k": PhotoImage(file="sprites/w_king.gif")
        }
        self.blank_sprite = PhotoImage(file="sprites/blank.gif")

        self.window.title("Chess")
        self.window.geometry(str(self.ts * 9) + "x" + str(self.ts * 9))

        self.draw_board()

        self.window.mainloop()

    def piece_sprite(self, color, piece_type):
        if color == "w":
            return self.w_sprite_dict[piece_type]
        elif color == "b":
            return self.b_sprite_dict[piece_type]
        else:
            return self.blank_sprite

    def draw_board(self):
        tiles = [[None for j in range(8)] for i in range(8)]
        Label(self.window, height=self.ts*10, width=self.ts*10, bg="white")

        for i in range(8):
            for j in range(8):
                sprite = self.piece_sprite(self.display.pieces()[i][j][0], self.display.pieces()[i][j][1])
                tiles[i][j] = Label(self.window, bd=2, height=self.ts, width=self.ts, image=sprite, bg=self.display.get_colors()[i][j])
                tiles[i][j].grid(row=i, column=j)
                tiles[i][j].image = sprite
                tiles[i][j].bind('<Button-1>', self.click(i, j))

    def click(self, x, y):
        return lambda event: self.run(x, y)

    def run(self, x, y):
        self.game.click(x, y)
        self.display.update()
        self.draw_board()

