import sys
from collections import deque
input = sys.stdin.readline


N,M = map(int,input().split())
graph = [list(map(int,input().strip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
def bfs(y,x):
    visited[y][x] = 1
    q = deque()
    q.append((y,x))
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]
    while q:
        ey,ex = q.popleft()
        if ey == N-1 and ex == M-1:
            print(visited[ey][ex])
            return
        for i in range(4):
            nx = dx[i] + ex
            ny = dy[i] + ey
            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] == 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = visited[ey][ex]+1
                    q.append((ny,nx))
bfs(0,0) #BFS 한번만 최단거리만 구함
