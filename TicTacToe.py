PGN = []

def displayBoard(board): #OK
    print(f"""
+-------+-------+-------+
|       |       |       |
|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |
|       |       |       |
+-------+-------+-------+
|       |       |       |
|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |
|       |       |       |
+-------+-------+-------+""")

def enterMove(board, move): #OK
    try: move = int(move)
    except: enterMove(board, input("\nEnter a valid (numeral) move: ")); return
    if move<=3: pos = 0, move-1
    elif move<=6: pos = 1, move-4
    elif move<=9: pos = 2, move-7
    else: enterMove(board, input("\nEnter a number from 1 to 9: ")); return
    if pos in listFree(board): 
        PGN.append(["O", list(pos)])
        board[pos[0]][pos[1]] = "O"
    else: enterMove(board, input("\nEnter an unoccupied place: ")); return

def listFree(board): #OK
    free = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if type(board[i][j]) is int: free.append((i, j))
    return free

def Wins(board, sign): #OK
    chances = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)], [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)], [(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]
    for x, y, z in chances:
        VICTORY = board[x[0]][x[1]] == sign and board[y[0]][y[1]] == sign and board[z[0]][z[1]] == sign
        if VICTORY: return True
    else: False

def COMP(board): #OK
    from random import choice
    if len(listFree(board))==9 or len(listFree(board))==8:
        all = [
            [0, 0],
            [2, 2],
            [2, 0],
            [0, 2]
        ]
        pos = choice(all)
        while type(board[pos[0]][pos[1]]) is str:
            all.remove(pos)
            pos = choice(all)
        PGN.append(["X", pos])
        board[pos[0]][pos[1]] = "X"
    else:
        chances = [
        [(0, 0), (0, 1), (0, 2)], 
        [(1, 0), (1, 1), (1, 2)], 
        [(2, 0), (2, 1), (2, 2)], 
        [(0, 0), (1, 0), (2, 0)], 
        [(0, 1), (1, 1), (2, 1)], 
        [(0, 2), (1, 2), (2, 2)], 
        [(0, 0), (1, 1), (2, 2)], 
        [(0, 2), (1, 1), (2, 0)]]
        for i in range(8):
            for j in range(3):
                x = chances[i][j]
                chances[i][j] = board[x[0]][x[1]]
        for k in chances:
            for l in ["O", "X"]:
                for m, n, o in [[0,1,2],[1,2,0],[2,0,1]]:
                    if k[m] == l and k[n] == l and type(k[o]) is int:
                        move = k[o]
                        if move<=3: move = 0, move-1
                        elif move<=6: move = 1, move-4
                        elif move<=9: move = 2, move-7
                        PGN.append(["X", list(move)])
                        board[move[0]][move[1]] = "X"
                        return
        for p in chances:
            for q, r, s in [[0,1,2],[1,2,0],[2,0,1]]:
                if p[q] == "X" and type(r) is int and type(s) is int:
                    move = p[choice([r, s])]
                    if move<=3: move = 0, move-1
                    elif move<=6: move = 1, move-4
                    elif move<=9: move = 2, move-7
                    PGN.append(["X", list(move)])
                    board[move[0]][move[1]] = "X"
                    return
        move = choice(listFree(board))
        PGN.append(["X", list(pos)])
        board[move[0]][move[1]] = "X"
        return

def __init__(): #ALL GOOD
    from random import choice   
    from time import sleep as _
    board = [[1, 2, 3], 
             [4, 5, 6], 
             [7, 8, 9]]
    chance = choice([True, False])
    # chance = True
    while len(listFree(board)) != 0:
        if chance:
            displayBoard(board)
            enterMove(board, input("\nEnter your move: "))
            chance = not chance
        else:
            displayBoard(board)
            COMP(board)
            chance = not chance
        if Wins(board, "X"): 
            print("\n--------------------------------------------------------")
            displayBoard(board)
            print("\nYou Lose... ")
            return
        elif Wins(board, "O"): 
            print("\n--------------------------------------------------------")
            displayBoard(board)
            print("\nYou Win! ")
            return
    displayBoard(board)
    print("Its a tie")

__init__() #RUN