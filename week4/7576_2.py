import sys
from collections import deque
input = sys.stdin.readline

'''
1. 토마토 익은 상태 1 - 익지않은 토마토 0 - 토마토가 들어있지않는 칸 -1
2. 토마토는 상하좌우 익지않은 토마토를 익게 함 * 토마토 1의 위치 상하좌우 탐색하면서 0이면 1로 바꾸고 그럼 되지않을까
'''

#상자의 크기
M,N = map(int,input().split()) #M -- x, N -- y
graph = [list(map(int,input().split())) for _ in range(N)]

q = deque()
#1토마토가 익은거부터해서 -- 안익은거 익게해야하니깐
for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                q.append((i,j))  #1 토마토의 위치가 Queue에
def bfs():
    
    while q:
        dx = [0,0,1,-1]
        dy = [-1,1,0,0]
        ey, ex = q.popleft()
        for i in range(4):
            nx = dx[i] + ex
            ny = dy[i] + ey
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = graph[ey][ex] + 1
                    q.append((ny,nx))
date = 0
bfs()
#최소일수 구하기
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(-1)
            exit(0)
        date = max(date,graph[i][j])
#1부터 시작한거라서 
print(date -1)
