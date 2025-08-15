import sys
from collections import deque
sys.setrecursionlimit(10000)

#상하좌우로 움직인 거리
dx = [0,0,1,-1]
dy = [-1,1,0,0]
#말처럼 움직인 거리
hy = [2,2,1,1,-2,-2,-1,-1]
hx = [1,-1,2,-2,1,-1,-2,2] 

def bfs():
    #방문여부
    queue = deque()
    #초기값 설정
    queue.append((0,0,0,0)) # y , x , 이동횟수, 말 이동 횟수
    visited[0][0][0] = 1
    while queue:
        y,x,dst,horse_used = queue.popleft()
        #종료(도착지점에 도달한 경우)ㅈ
        if y == H-1 and x == W-1:
            return dst
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < H and 0 <= nx < W:
                if graph[ny][nx] == 0 and not visited[ny][nx][horse_used]:
                    visited[ny][nx][horse_used] = 1
                    queue.append((ny,nx,dst+1,horse_used))
        if horse_used < K: #말로 이동가능
            for h in range(8):
                ny = y + hy[h]
                nx = x + hx[h]
                if 0 <= ny < H and 0 <= nx < W:
                    if graph[ny][nx] == 0 and not visited[ny][nx][horse_used + 1]:
                            visited[ny][nx][horse_used+1] = 1
                            queue.append((ny,nx,dst+1,horse_used+1))
    return -1
#말의 움직임이 가능한 횟수
K = int(sys.stdin.readline())
#체스판 크기 가로 W , 세로 H
W,H = map(int,sys.stdin.readline().split())
#체스판
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(H)]

visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]
print(bfs())
            

    
