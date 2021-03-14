chessBoard = {'a1': 'btower',
              'b1': 'brunner',
              'c1': 'bbishop',
              'd1': 'bqueen',
              'e1': 'bking',
              'f1': 'bbishop',
              'g1': 'brunner',
              'h1': 'btower',
              'a2': 'bpawn',
              'b2': 'bpawn',
              'c2': 'bpawn',
              'd2': 'bpawn',
              'e2': 'bpawn',
              'f2': 'bpawn',
              'g2': 'bpawn',
              'h2': 'bpawn',
              'a8': 'wtower',
              'b8': 'wrunner',
              'c8': 'wbishop',
              'd8': 'wking',
              'e8': 'wqueen',
              'f8': 'wbishop',
              'g8': 'wrunner',
              'h8': 'wtower',
              'a7': 'wpawn',
              'b7': 'wpawn',
              'c7': 'wpawn',
              'd7': 'wpawn',
              'e7': 'wpawn',
              'f7': 'wpawn',
              'g7': 'wpawn',
              'h8': 'wpawn',}


def validator(board):
    black = 'b'
    white = 'w'
    blackBricks = []
    whiteBricks = []
    validSpaceLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'e', 'g', 'h']
    validSpaceNumbers = [x for x in range(1, 9)]

    boardLetters = [key for (key, value) in board]
    for letter in boardLetters:
        if letter in validSpaceLetters:
            print("succes")
        else:
            print("not valid")

    for k, v in board.items():
        if black in v[0:1]:
            blackBricks.append((k, v))
        if white in v[0:1]:
            whiteBricks.append((k,v))

        if int(k[1:2]) in validSpaceNumbers:
            print("space numbers is correct")
        else:
            print("not correct numbers space")

    countB = len(blackBricks)
    countW = len(whiteBricks)

    if countB != 16 or countW != 16:
        print("Players doesn't have the right amount of bricks")
    else:
        print("players have the right amount of bricks")

    print(validSpaceNumbers)



validator(chessBoard)