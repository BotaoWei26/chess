def detect_block(move, place, pieces):
    for piece in pieces:
        if piece in [[x, place[1]] for x in (list(range(move[0] + 1, place[0])) + list(range(place[0] + 1, move[0])))]:
            return True
    return False


print(detect_block([1,0],[5,0],[[0,0],[3,0]]))  #true
print(detect_block([1,0],[5,0],[[0,0]]))  #false
print(detect_block([5,0],[1,0],[[0,0],[3,0]]))  #true
print(detect_block([0,0],[2,0],[[1,0]]))  #true
print(detect_block([2,0],[0,0],[[1,0]]))  #true
print(detect_block([0,0],[1,0],[[2,0]]))  #false
print(detect_block([1,0],[0,0],[[2,0]]))  #false
print(detect_block([0,0],[5,0],[[0,0],[3,0]]))  #true
print(detect_block([3,0],[5,0],[[0,0],[3,0]]))  #true