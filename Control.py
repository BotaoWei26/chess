from Game import *
from TextDisplay import *


class Control:
    def __init__(self):
        self.game = Game()
        self.display = TextDisplay()

    def read_line(self, read):
        print(read)
