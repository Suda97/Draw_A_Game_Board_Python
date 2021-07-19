def floor(boardsize):
    print(" --- " * boardsize)

def wall(boardsize):
    print("|    " * (boardsize + 1))


if __name__ == '__main__':
    size = int(input("What size of board? "))

    for index in range(size):
        floor(size)
        wall(size)
    floor(size)