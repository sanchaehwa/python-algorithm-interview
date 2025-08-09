import sys
from collections import deque
input = sys.stdin.readline

def bfs(q):
    dz = [-1, 1, 0, 0, 0, 0]  # 위, 아래
    dy = [0, 0, -1, 1, 0, 0]  # 앞, 뒤 (세로)
    dx = [0, 0, 0, 0, -1, 1]  # 왼, 오 (가로)
    while q:
        ez,ey,ex = q.popleft()
        for i in range(6):
            nz = ez + dz[i]
            ny = ey + dy[i]
            nx = ex + dx[i]
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
                if tomatoes[nz][ny][nx] == 0:
                    tomatoes[nz][ny][nx] = tomatoes[ez][ey][ex] + 1
                    q.append((nz,ny,nx))

M,N,H = map(int,input().split())
tomatoes = [] #전체 토마토 밭
#3차원 배열 입력받기
for _ in range(H):
    layer = [] #한층
    for _ in range(N):
        row = list(map(int,input().split()))
        layer.append(row)
    tomatoes.append(layer)
#방문 여부
#시작점
q = deque()

for h in range(H):
    for n in range(N):
        for m in range(M):
            #익은 토마토인 경우에는 전부 큐에 넣고
            if tomatoes[h][n][m] == 1:
                q.append((h,n,m))
bfs(q)
max_days = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomatoes[h][n][m] == 0:
                print(-1)
                sys.exit() #종료
            max_days = max(max_days, tomatoes[h][n][m])
print(max_days-1)
            