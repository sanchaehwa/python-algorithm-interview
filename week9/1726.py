import sys
from collections import deque
input = sys.stdin.readline

def bfs(ny,nx,nd,ey,ex,ed):
    q = deque()
    q.append((ny-1,nx-1,nd))
    visited = [[[0] * 5 for _ in range(N)] for _ in range(M)]
    visited[ny][nx][nd] = 1
    direction = [(0,1),(0,-1),(1,0),(-1,0)]

    while q:
        y,x,d = q.popleft()
        my,mx = direction[d-1]
        if y == ey-1 and x == ex-1 and d == ed:
            print(visited[y][x][d]-1)
            return
        #상화좌우
        for i in range(1,4):
            ty = y + my * i
            tx = x + mx * i
            if not (0 <= tx < N and 0 <= ty < M):
                break
            if graph[ty][tx] == 1:
                break
            
            if graph[ty][tx] == 0 and not visited[ty][tx][d]:
                visited[ty][tx][d] = visited[y][x][d] + 1
                q.append((ty,tx,d))
        left_turn = [0,4,3,2,1]
        right_turn = [0,3,4,2,1]
        for nd in [left_turn[d],right_turn[d]]:
            if not visited[y][x][nd]:
                visited[y][x][nd] = visited[y][x][d] + 1
                q.append((y,x,nd))

'''
- 세로 M / 가로 N
- 궤도 설치 그래프
- 현재위치 + 방향
- 도달해야할 위치 + 방향
'''
M,N = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(M)]
ny,nx,nd = map(int,input().split())
ey,ex,ed = map(int,input().split())
bfs(ny,nx,nd,ey,ex,ed)