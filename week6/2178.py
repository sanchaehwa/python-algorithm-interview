import sys
from collections import deque

input = sys.stdin.readline

def bfs(y,x):
    q = deque()
    q.append((y,x))
    visited[y][x] = 1
    while q:
        dx = [0,0,1,-1]
        dy = [-1,1,0,0]
        ey,ex = q.popleft()
        if ey == (N-1) and ex == (M-1):
            print(visited[ey][ex])
            return
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = visited[ey][ex] + 1
                    q.append((ny,nx))

N,M = map(int,input().split())
graph = [list(map(int,input().strip())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
bfs(0,0) #시작 위치
