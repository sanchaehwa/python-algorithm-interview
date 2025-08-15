import sys
from collections import deque
from itertools import combinations
import copy

input = sys.stdin.readline

N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)] 
#상하좌우 탐색
dy = [-1,1,0,0]
dx = [0,0,1,-1]

def bfs(temp):
    q = deque()
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 2: #바이러스
                q.append((i,j))
    while q:
        ey,ex = q.popleft() 
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if temp[ny][nx] == 0:
                    temp[ny][nx] = 2
                    q.append((ny,nx))
    safe = sum(row.count(0) for row in temp) #0인 요소만 추출한다는것
    return safe


#0인공간을 찾고 3개 뽑고 -- 벽을 세운뒤 -- bfs 안전영역을 구하기
max_safe = 0
blanks = [(i,j) for i in range(N) for j in range(M) if graph[i][j] == 0]
for w in combinations(blanks,3):
    temp = copy.deepcopy(graph) #graph 복사
    for y, x in w:
        temp[y][x] = 1 # 3개를 벽을 세운뒤
    safe = bfs(temp)
    max_safe = max(max_safe,safe)
print(max_safe)