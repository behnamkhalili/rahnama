n = int(input()) # jadval
m = int(input()) # bazikon
res = True
board = [[0]*n]*n

def checkwinner(board, n):

    # satr
    checker = 0
    for j in range(n):
        test = board[0][j]
        for k in range(n-1):
            if test == board[k+1][j]:
                checker += 1
        if checker == n-1:
            return False

    # sotoon
    checker = 0
    for j in range(n):
        test = board[j][0]
        for k in range(n-1):
            if test == board[j][k+1]:
                checker += 1
        if checker == n-1:
            return False
    
    # ghotr 1
    checker = 0
    test = board[0][0]
    for j in range(n-1):
        if test == board[j+1][j+1]:
            checker += 1
    if checker == n-1:
        return False

    # ghotr 2
    checker = 0
    test = board[0][n]
    for j in range(n-1):
        if test == board[j+1][n-j-1]:
            checker += 1
    if checker == n-1:
        return False

    return 'draw'

while res:
    for i in range(m):
        cell = list(map(int, input().strip().split()))
        board[cell[0]][cell[1]] = i + 1
        res = checkwinner(board, n)
        if res == 'draw':
            print('draw')
            res = False
            break
        if not res:
            winner = i + 1
            print(winner, 'is winner')
            break

for i in board:
    print(i)
    #print('\n')