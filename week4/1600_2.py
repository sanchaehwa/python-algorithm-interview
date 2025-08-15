import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append((0,0,0,1))
    visited[0][0][0] = 1 #방문처리
    #원숭이 움직임
    dy = [-1,1,0,0]
    dx = [0,0,1,-1]
    #말의 움직임
    hy = [2,2,1,1,-2,-2,-1,-1]
    hx = [1,-1,2,-2,1,-1,-2,2]
    while q:
        y,x,horse_used,c = q.popleft()
        if y == H-1 and x == W-1:
            return c
        for i in range(4):
            ey = dy[i] + y
            ex = dx[i] + x
            if 0 <= ey < H and 0 <= ex < W:
                if graph[ey][ex] == 0 and visited[ey][ex][horse_used] == 0: #방문하지않은경우
                    visited[ey][ex][horse_used] = 1
                    q.append((ey,ex,horse_used,c+1))
        if horse_used < K : #말 움직일수있더
            for i in range(8):
                cy = hy[i] + y
                cx = hx[i] + x
                if 0 <= cy < H and 0 <= cx < W:
                    if not visited[cy][cx][horse_used+1]: #말은 장애물을 뛰어넘을수도 있다
                        visited[cy][cx][horse_used+1] = 1
                        q.append((cy,cx,horse_used +1,c+1))
    return -1
K = int(input()) #말로 이동할 수 있는 횟수
W,H = map(int,input().split()) #W : 가로길이, H: 세로길이 
graph = [list(map(int,input().split())) for _ in range(H)]
#방문 여부 
visited = [[[0] * (K+1) for _ in range(W)] for _ in range(H)]
print(bfs())