import sys
sys.setrecursionlimit(10**6)
def dfs(x,y):
    visited[x][y] = True
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    size =1
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < M and 0 <= ny < N:
            if not visited[nx][ny] and graph[nx][ny] == 0:
                size += dfs(nx,ny)
    return size
M,N,K = map(int,sys.stdin.readline().split())
    
graph = [[0] * N for _ in range(M)]
for _ in range(K):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    for y in range(y1,y2):
        for x in range(x1,x2):
            graph[y][x] = 1 #칠해져있는 영역
result = []
cnt = 0
visited = [[False] * N for _ in range(M)]
for x in range(M):
    for y in range(N):
        if graph[x][y] == 0 and not visited[x][y]:
            area = dfs(x,y)
            result.append(area)
            cnt += 1
print(cnt)
print(' '.join(map(str,sorted(result))))
