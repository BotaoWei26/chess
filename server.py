import socket

with socket.socket() as s:
    s = socket.socket()

    s.bind(('localhost', 9999))

    s.listen(2)
    print("waiting for connections...")

    white, white_addr = s.accept()
    print("White player is connected on: ", white_addr)

    black, black_addr = s.accept()
    print("Black player is connected on: ", white_addr)

    white.send(bytes("w","utf-8"))
    black.send(bytes("b","utf-8"))
    while True:
        black.send(white.recv(1024))
        white.send(black.recv(1024))




