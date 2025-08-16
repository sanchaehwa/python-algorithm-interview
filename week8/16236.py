'''
- 자기랑 같은 무게의 물고기 먹으면 +1
- 자기랑 같거나 작은 물고기만 지나갈수 있음
- 9 : 아기 상어 위치
- 1,2,3,4,5,6: 물고기 크기
- 0: 빈칸
- 더이상 먹을거 없으면 print
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(y,x,kg):
    q = deque()
    q.append((y,x))
    visited = [[-1] * N for _ in range(N)]
    visited[y][x] = 0
    ny = [-1,1,0,0]
    nx = [0,0,1,-1]
    fishes = []
    while q:
        sy,sx = q.popleft() #y - x
        for i in range(4):
            ey = ny[i] + sy
            ex = nx[i] + sx
            if 0 <= ey < N and 0 <= ex < N and visited[ey][ex] == -1:
                if graph[ey][ex] <= kg: #지나갈수있는 조건
                    visited[ey][ex] = visited[sy][sx] + 1
                    q.append((ey,ex))
                if 0 < graph[ey][ex] < kg:
                    fishes.append((visited[ey][ex],ey,ex))
    if not fishes:
        return None
    fishes.sort()
    return fishes[0]

#공간의 크기
N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
#아기상어 위치
target = 9
position = None
for i, row in enumerate(graph):
    for j, value in enumerate(row):
        if value == target:
            position = (i,j)
            break
        if position:
            break
y,x = position

fy,fx = y,x
kg = 2
eat = 0
time = 0

while True:
    result = bfs(fy,fx,kg)
    if result is None:
        break
    dist,ry,rx = result
    time += dist
    fy,fx = ry,rx
    graph[fy][fx] = 0
    eat += 1
    if eat == kg:
        kg += 1
        eat = 0
print(time)

