from Graphics import Graphics
import socket


class Client(Graphics):
    def __init__(self, window, ts):
        super().__init__(window, ts)

        self.c = socket.socket()
        self.c.connect(('localhost', 9999))

        self.game_state = None
        self.pick = None
        self.move = None

        self.color = self.c.recv(128).decode()

        if self.color == 'b':
            self.listen()

    def run(self, x, y):
        self.game_state = self.game.click(x, y, self.color)
        self.display.update()
        self.draw_board()
        if self.game_state is not None:
            if self.game_state[0] == "pick":
                self.pick = self.game_state[1]
            elif self.game_state[0] == "move":
                self.move = self.game_state[1]
                self.send()

    def send(self):
        print(self.pick, self.move)
        self.c.send(bytes(str(self.pick[0]) + str(self.pick[1]) + str(self.move[0]) + str(self.move[1]), "utf-8"))
        self.listen()

    def listen(self):
        data = self.c.recv(128).decode()
        self.game.click(int(data[0]), int(data[1]))
        self.game.click(int(data[2]), int(data[3]))
        self.display.update()
        self.draw_board()
