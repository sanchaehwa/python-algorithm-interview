import sys
sys.setrecursionlimit(10**6)

def dfs(i,j):
    visited[i][j] = 1
    dx = [0, 0, 1, -1, -1, -1, 1, 1]
    dy = [-1, 1, 0, 0, -1, 1, -1, 1] 
    for k in range(8):
        x = j + dx[k]
        y = i + dy[k]
        if 0 <= x < N and 0 <= y < M:
            if graph[y][x] == 1 and not visited[y][x]:
                dfs(y,x)

M,N = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split()))for _ in range(M)]
visited = [[0]*N for _ in range(M)]
cnt = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:
            dfs(i,j)
            cnt += 1
print(cnt)