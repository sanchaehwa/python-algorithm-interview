import sys
input = sys.stdin.readline

def dfs(y,x):
    visited[y][x] = 1
    dy = [-1,1,0,0]
    dx = [0,0,1,-1]
    depth = 1
    for i in range(4):
        ey = dy[i] + y
        ex = dx[i] + x
        if 0 <= ey < N and 0 <= ex < N:
            if not visited[ey][ex] and graph[ey][ex] == 1:
                depth += dfs(ey,ex)
    return depth


N = int(input())
graph = [list(map(int,input().strip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnt = 0
result = []
depth = 1
for y in range(N):
    for x in range(N):
        if not visited[y][x] and graph[y][x] == 1:
            result.append(dfs(y,x))
            cnt += 1
print(cnt)
for r in result:
    print(r)