import sys
from collections import deque
input = sys.stdin.readline

#방의수
N = int(input())
#전체 방
graph = [list(map(int,input().strip())) for _ in range(N)]
#방문
visited = [[-1] * N for _ in range(N)]
#start = (0,0)
def bfs(y,x):
    visited[y][x] = 0 #시작점 방문처리
    q = deque()
    q.append((y,x))
    dy = [-1,1,0,0]
    dx = [0,0,1,-1]
    while q:
        ey,ex = q.popleft() #현재 위치 : ey,ex
        for i in range(4):
            ny = ey +dy[i]
            nx = ex +dx[i]
            if 0 <= ny < N and 0 <= nx < N: #이동
                if graph[ny][nx] == 1: #흰방
                    if visited[ny][nx] == -1 or visited[ny][nx] > visited[ey][ex]:
                        visited[ny][nx] = visited[ey][ex]
                        q.appendleft((ny,nx)) #흰방 우선탐색
                else:
                    if visited[ny][nx] == -1 or visited[ny][nx] > visited[ey][ex] +1:
                        visited[ny][nx] = visited[ey][ex] + 1
                        q.append((ny,nx))
    #끝까지 도달했을떄 visited[N-1][N-1]
    print(visited[N-1][N-1])
bfs(0,0)