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
        self.board_sprite_dict = {
            "w": PhotoImage(file="sprites/player_turn_w.gif"),
            "b": PhotoImage(file="sprites/player_turn_b.gif"),
            "check": PhotoImage(file="sprites/check.gif"),
            "checkmate": PhotoImage(file="sprites/checkmate.gif"),
            "stalemate": PhotoImage(file="sprites/stalemate.gif"),
            "nothing": PhotoImage(file="sprites/blank.gif")
        }
        self.blank_sprite = PhotoImage(file="sprites/blank.gif")

        self.window.title("Chess")
        self.window.geometry(str(self.ts * 12) + "x" + str(self.ts * 12))

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

        top_boarder = Label(self.window, bd=0, height=self.ts*2, width=self.ts*12, image=self.board_sprite_dict[self.game.turn], bg='white')
        top_boarder.grid(row=0, column=0, rowspan=2, columnspan=12)
        bottom_boarder = Label(self.window, bd=0, height=self.ts*2, width=self.ts*12, image=self.board_sprite_dict[self.game.check_game_over()], bg='white')
        bottom_boarder.grid(row=10, column=0, rowspan=2, columnspan=12)
        left_boarder = Label(self.window, bd=0, height=self.ts*8, width=self.ts*2, image=self.blank_sprite, bg='white')
        left_boarder.grid(row=2, column=0, rowspan=8, columnspan=2)
        right_boarder = Label(self.window, bd=0, height=self.ts*8, width=self.ts*2, image=self.blank_sprite, bg='white')
        right_boarder.grid(row=2, column=10, rowspan=8, columnspan=2)

        for i in range(8):
            for j in range(8):
                sprite = self.piece_sprite(self.display.pieces()[i][j][0], self.display.pieces()[i][j][1])
                tiles[i][j] = Label(self.window, bd=0, height=self.ts, width=self.ts, image=sprite, bg=self.display.get_colors()[i][j])
                tiles[i][j].grid(row=i+2, column=j+2)
                tiles[i][j].bind('<Button-1>', self.click(i, j))

    def click(self, x, y):
        return lambda event: self.run(x, y)

    def run(self, x, y):
        self.game.click(x, y)
        self.display.update()
        self.draw_board()

