import sys
from collections import deque
input = sys.stdin.readline

def dfs(y,x):
    dy = [-1,0,1]
    dx = [1,1,1]
    visited[y][x] = True
    if x == C-1:
        return True
    for i in range(3):
        ey = dy[i] + y
        ex = dx[i] + x
        if 0 <= ey < R and 0 <= ex < C:
            if graph[ey][ex] == '.' and not visited[ey][ex]:
                if dfs(ey,ex):
                    return True

R,C = map(int,input().split())
graph = [list(input().strip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
result = 0
#첫째열에서 시작해야한다 
for i in range(R):
    if graph[i][0] == '.':
        if dfs(i,0):
            result += 1
print(result)