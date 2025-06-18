import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    visited[x][y] = True
    #같은 열에 있을때
    if board[x][y] == "|":
        if x+1 < n and board[x+1][y] == '|' and visited[x+1][y]==False:
            dfs(x+1,y)
        else:
            return 
        #같은 행에 있을때
    if board[x][y] == "-":
        if y+1<m and board[x][y+1] == "-" and visited[x][y+1]==False:
            dfs(x,y+1)
        else:
            return
            

#N,M 입력
n, m = map(int,input().split())
#Board에 N , M 크기로 넣기
board = [list(input().strip()) for _ in range(n)]
cnt = 0 #개수

visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if visited[i][j] == False:
            dfs(i,j)
            cnt += 1
print(cnt)

