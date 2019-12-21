from Game import *
from TextDisplay import *


class Control:
    def __init__(self):
        self.game = Game()
        self.display = TextDisplay(self.game)

    def read_line(self, read):
        read = read.split()
        print(read)

        if read[0].lower() == "pick":
            if not self.game.pick(int(read[1]), int(read[2])):
                print("Wrong player's turn")
        elif read[0].lower() == "move":
            if not self.game.move(int(read[1]), int(read[2])):
                print("Not a valid move")
        else:
            print("Incorrect Input")

        self.display.update()
        self.display.display()
