import sys

# def dfs(y,x):
#     dx = [0,0,1,-1]
#     dy = [-1,1,0,0]
#     visited[y][x] = 1
#     cnt = 0
#     for i in range(4):
#         ny = y + dy[i]
#         nx = x + dx[i]
#         if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
#             if candy[y][x] != candy[ny][nx] :
#                 candy[y][x],candy[ny][nx] = candy[ny][nx],candy[y][x]
#             dfs(ny,nx)

#             #



# N = int(sys.stdin.readline())
# candy = [list(sys.stdin.readline().strip()) for _ in range(N)]
# visited = [[0]*N for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         if not visited[i][j]:
#             dfs(i,j)

import sys
sys.setrecursionlimit(10**7)

def calculate_max_sequence(board):
    max_len = 1
    # 가로 검사
    for y in range(N):
        count = 1
        for x in range(1, N):
            if board[y][x] == board[y][x-1]:
                count += 1
            else:
                max_len = max(max_len, count)
                count = 1
        max_len = max(max_len, count)
    # 세로 검사
    for x in range(N):
        count = 1
        for y in range(1, N):
            if board[y][x] == board[y-1][x]:
                count += 1
            else:
                max_len = max(max_len, count)
                count = 1
        max_len = max(max_len, count)
    return max_len

N = int(sys.stdin.readline())
candy = [list(sys.stdin.readline().strip()) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]

max_result = 1

for i in range(N):
    for j in range(N):
        for d in range(4):
            ni = i + dy[d]
            nj = j + dx[d]
            if 0 <= ni < N and 0 <= nj < N and candy[ni][nj] != candy[i][j]: #c -- p 
                candy[i][j], candy[ni][nj] = candy[ni][nj], candy[i][j] #swap
                max_result = max(max_result, calculate_max_sequence(candy))
                candy[i][j], candy[ni][nj] = candy[ni][nj], candy[i][j] 

print(max_result)