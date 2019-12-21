from Game import *
from TextDisplay import *
from cordDictionary import *


class Control:
    def __init__(self):
        self.game = Game()
        self.display = TextDisplay(self.game)

    def read_line(self, read):
        read = read.split()
        print(read)

        if read[0].lower() == "pick":
            if not self.game.pick(cord_row[read[2]], cord_col[read[1]]):
                print("Wrong player's turn")
        elif read[0].lower() == "move":
            if not self.game.move(cord_row[read[2]], cord_col[read[1]]):
                print("Not a valid move")
        else:
            print("Incorrect Input")

        self.display.update()
        self.display.display()
