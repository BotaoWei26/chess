from Game import *
from TextDisplay import *


class Control:
    def __init__(self):
        self.game = Game()
        self.display = TextDisplay(self.game)

    def read_line(self, read):
        print(read)
        if read == "test_move":
            self.game.test_move()
        self.display.update()
        self.display.display()
