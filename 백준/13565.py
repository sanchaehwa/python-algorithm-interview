import sys
sys.setrecursionlimit(10**6)  

def dfs(x,y):
    visited[x][y] = True
    #상하좌우 탐색
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        nx,ny = dx[i] + x,dy[i] + y
        if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and graph[nx][ny] == 0:
            dfs(nx,ny)

M,N = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().strip()))for _ in range(M)]
visited = [[False] *N for _ in range(M)]

for i in range(N):
    if graph[0][i] == 0 and not visited[0][i]:
        dfs(0,i)
##Inner 은 맨끝 - 방문할수있으면 침투한거
if True in visited[M-1]:
    print("YES")
else:
    print("NO")