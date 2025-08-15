import sys
from collections import deque
input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,1,-1]

def graphA_bfs(y,x):
    now = graphA[y][x]
    visited1[y][x] = True
    q = deque()
    q.append((y,x))
    while q:
        ey,ex = q.popleft()
        for i in range(4):
            ny = dy[i] + ey
            nx = dx[i] + ex
            if 0 <= ny < N and 0 <= nx < N:
                if graphA[ny][nx] == now and not visited1[ny][nx]:
                    q.append((ny,nx))
                    visited1[ny][nx] = True

def graphB_bfs(y,x):
    now = graphB[y][x]
    visited2[y][x] = True
    q = deque()
    q.append((y,x))
    while q:
        ey,ex = q.popleft()
        for i in range(4):
            ny = dy[i] + ey
            nx = dx[i] + ex
            if 0 <= ny < N and 0 <= nx < N:
                if graphB[ny][nx] == now and not visited2[ny][nx]:
                    q.append((ny,nx))
                    visited2[ny][nx] = True


N = int(input())
graphA = [list(input().strip()) for _ in range(N)] #적록색약이 아닌 사람
graphB = [[c if c != 'G' else 'R' for c in row] for row in graphA] #적록색약

visited1 = [[False] * N for _ in range(N)]
cnt1 = 0
visited2 = [[False] * N for _ in range(N)]
cnt2 = 0

for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            graphA_bfs(i,j)
            cnt1 += 1

for i in range(N):
    for j in range(N):
        if not visited2[i][j]:
            graphB_bfs(i,j)
            cnt2 += 1

print(cnt1,cnt2)
