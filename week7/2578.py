import sys
input = sys.stdin.readline
#1-5번째까지 빙고판 / 6 - 10째까지 사회자가 부른 수
ipt = [list(map(int,input().split())) for _ in range(10)]
board = [ipt[i] for i in range(5)]
speek = [ipt[i] for i in range(5,10)]

result = 0
for s in speek:
    for num in s: 
        for i in range(5):
            for j in range(5):
                if board[i][j] == num:
                    board[i][j] = 0

def count_bingo(board):
    bingo = 0
    for row in board: #가로
        if row.count(0) == 5:
            bingo += 1
    for col in zip(*board):
        #list
        if list(col).count(0) == 5:
            bingo += 1
    if all(board[i][i] == 0 for i range(5)):
        bingo += 1
    if all(board[i][4-i] == 0 for i in range(5)):
        bingo += 1
    return bingo 

