import sys
from collections import deque
input = sys.stdin.readline

def bfs(y,x):
    q =  deque()
    q.append((y,x))
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]
    while q:
        ny,nx = q.popleft()
        for i in range(4):
            ey = ny + dy[i]
            ex = nx + dx[i]
            if 0 <= ey < N and 0 <= ex < N:
                if not visited[ey][ex] and graph[ey][ex] > N:
                    visited[ey][ex] = 1
                    q.append((ey,ex))

N = int(input())
if N == 0:
    print(0) 
    exit()
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnt = 0
for y in range(N):
    for x in range(N):
        if graph[y][x] > N and not visited[y][x]:
            bfs(y,x)
            cnt +=1 
print(cnt)