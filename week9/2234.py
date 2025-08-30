'''
이 성에 있는 방의 개수
가장 넓은 방의 넓이
하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
'''
import sys
from collections import deque
input = sys.stdin.readline


def bfs(y,x,room_id):

    visited[y][x] = room_id
    size = 1
    q = deque()
    q.append((y,x))

    my = [-1,1,0,0]
    mx = [0,0,1,-1]
    
    while q:
        sy,sx,


#x -- y
N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(M)]
lst = [[[] for _ in range(N)] for _ in range(M)]
visited = [[0]*N for _ in range(M)]

# 서쪽 : 1 (0,-1), 북쪽 : 2 (-1,0) , 동쪽 : 4 (0,1) , 남쪽 : 8 (1,0)
for i in range(M):
    for j in range(N):
        cell = graph[i][j]
        lst[i][j] = []
        if ((cell & 1) == 0):
            lst[i][j].append((0,-1))
        if ((cell & 2) == 0):
            lst[i][j].append((-1,0))
        if((cell & 4) == 0):
            lst[i][j].append((0,1))
        if((cell & 8) == 0):
            lst[i][j].append((1,0))

result = []
room_size = []
broken = 1
for i in range(M):
    for j in range(N):
        if visited[i][j] == 0:
            room_id += 1
            size = bfs(i,j,room_id)
            room_size.append(size)
print(room_id)
print(max(room_size))
        