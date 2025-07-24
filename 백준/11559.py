import sys
from collections import deque
input = sys.stdin.readline

graph = [list(input().rstrip()) for _ in range(12)]
dy = [-1,1,0,0]
dx = [0,0,1,-1]    

# BFS를 통해 인접한 같은 색 뿌요 그룹 탐색
def bfs(y,x):
    q = deque([(y,x)])
    now = graph[y][x] # 현재 뿌요 색깔
    visited[y][x] = True
    pos = [(y,x)]
    while q:
        ny,nx = q.popleft()
        for i in range(4):
            ey = dy[i] + ny
            ex = dx[i] + nx
            if 0 <= ey < 12 and 0 <= ex < 6:
                if graph[ey][ex] == now and not visited[ey][ex]:
                    visited[ey][ex] = True
                    pos.append((ey,ex))
                    q.append((ey,ex))
    return pos if len(pos) >= 4 else []  # 4개 이상 연결됐을 때만 반환

# 중력 적용
def drop():
    for x in range(6):
        stack = []
        for y in range(11,-1,-1):  # 아래에서부터 탐색
            if graph[y][x] != '.':
                stack.append(graph[y][x])
        for y in range(11,-1,-1):  # 다시 아래에서 채우기
            graph[y][x] = stack.pop(0) if stack else '.'

# 연쇄 수
cnt = 0
while True:
    visited = [[False]*6 for _ in range(12)]
    bomb = []

    for y in range(12):
        for x in range(6):
            if not visited[y][x] and graph[y][x] != '.':
                result = bfs(y,x)
                if result:
                    bomb.extend(result)  # 여러 그룹을 누적해야 함

    if not bomb:
        break

    for y,x in bomb:
        graph[y][x] = '.'

    drop()
    cnt += 1

print(cnt)