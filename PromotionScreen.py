from tkinter import *

##doesnt work cause threading,.....

class PromotionScreen:
    def __init__(self):
        self.type = None
        self.root = Tk()
        queenButton = Button(self.root, text="QUEEN", command=self.queen)
        queenButton.pack()
        knightButton = Button(self.root, text="KNIGHT", command=self.knight)
        knightButton.pack()
        rookButton = Button(self.root, text="ROOK", command=self.rook)
        rookButton.pack()
        bishopButton = Button(self.root, text="BISHOP", command=self.bishop)
        bishopButton.pack()
        self.root.mainloop()

    def queen(self):
        self.type = "queen"
        self.root.destroy()

    def knight(self):
        self.type = "knight"
        self.root.destroy()

    def rook(self):
        self.type = "rook"
        self.root.destroy()

    def bishop(self):
        self.type = "bishop"
        self.root.destroy()

    def get(self):
        return self.type
