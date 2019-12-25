def detect_block(move, place, pieces):
    block = []

    if (move[0] > place[0]) and (move[1] > place[1]):
        for i in range(move[0] - place[0]):
            block.append([place[0]+i, place[1]+i])

    if (move[0] > place[0]) and (move[1] < place[1]):
        for i in range(move[0] - place[0]):
            for j in range(place[1] - move[1]):
                block.append([place[0]+i, place[1]-j])

    if (move[0] < place[0]) and (move[1] > place[1]):
        for i in range(place[0] - move[0]):
            for j in range(move[1] - place[1]):
                block.append([place[0]-i, place[1]+j])

    elif (move[0] < place[0]) and (move[1] < place[1]):
        for i in range(place[1] - move[1]):
            block.append([place[0]-i, place[1]-i])

    for piece in pieces:
        if piece in block:
            return True
    return False


print(detect_block([2,2],[0,0],[[1,1]]))  #true
print(detect_block([0,2],[2,0],[[1,1]]))  #true
print(detect_block([2,0],[0,2],[[1,1]]))  #true
print(detect_block([0,0],[2,2],[[1,1]]))  #true

print(detect_block([3,2],[1,0],[[2,1]]))  #true
print(detect_block([1,2],[3,0],[[2,1]]))  #true
print(detect_block([3,0],[1,2],[[2,1]]))  #true
print(detect_block([1,0],[3,2],[[2,1]]))  #true
