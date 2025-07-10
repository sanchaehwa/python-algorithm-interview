import sys
from collections import deque
input = sys.stdin.readline
'''
1. 아이디어
    - 2중 For문을 돌면서 1인지점을 찾고 1인 지점부터 탐색
    - bfs() 수행할때마다 +1 -> 익은 토마토 개수
    - 1이 없는 경우 -> -1
    - 모든 토마토가 익은 경우 -> 1 (0이 아닌 경우면 queue에 append를 하지않으면 되는거 아닌가..?)
    - 그리고 -1은 취급하지말고
'''


M,N = map(int,input().split()) #M - x N - y
graph = [list(map(int,input().split())) for _ in range(N)]

q = deque()
    #1인 걸 Queue에 다 넣기 (익은 토마토의 위치를)
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append((i,j))
def bfs():
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]
    while q:
        ey,ex = q.popleft()
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = graph[ey][ex] + 1
                    q.append((ny,nx))
bfs()
day = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(-1)
            exit(0)
        day = max(day,graph[i][j])
#0이 아닌 1부터 시작을 했으니깐 -
print(day - 1)
    



