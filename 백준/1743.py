import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
def dfs(x,y):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    cnt = 1
    visited[y][x] = 1
    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if 0 <= x1 < M and 0 <= y1 < N:
            if not visited[y1][x1] and graph[y1][x1] == 1:
                cnt += dfs(x1,y1)
    return cnt

N,M,K = map(int,input().split())

graph = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
cnt = 0
result = []
for _ in range(K):
    R,C = map(int,input().split())
    graph[R-1][C-1] = 1
for y in range(N):
    for x in range(M):
        if visited[y][x] == 0 and graph[y][x] == 1:
            result.append(dfs(x,y))
print(max(result))