import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

def bfs(s,sy,sx,ey,ex):
    visited = [[0] * s for _ in range(s)]
    #나이트의 움직임 
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]
    q = deque()
    q.append((sy,sx))
    while q:
        y,x = q.popleft()
        if y == ey and x == ex:
            print(visited[ey][ex])
            return
        for i in range(8):
            ny = dy[i] + y
            nx = dx[i] + x
            if 0 <= ny < s and 0 <= nx < s:
                if visited[ny][nx] == 0: #방문하지않은 경우
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny,nx))


for _ in range(T):
    #체스판의 크기
    S = int(input())
    graph = [[0] * S for _ in range(S)]
    #시작지점
    sy,sx = map(int,input().split())
    #도달해야할 지점
    ey,ex = map(int,input().split())
    #bfs로 탐색
    bfs(S,sy,sx,ey,ex)