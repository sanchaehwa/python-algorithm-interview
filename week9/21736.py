import sys
from collections import deque
input = sys.stdin.readline




def bfs(y,x):
    q = deque()
    q.append((y,x))
    visited[y][x] = 1
    count = 0
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]
    while q:
        ey,ex = q.popleft()
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] != "X" and not visited[ny][nx]:
                    if graph[ny][nx] == "P":
                        count += 1
                    q.append((ny,nx))
                    visited[ny][nx] =1
    return count
                    

#캠퍼스의 크기
N,M = map(int,input().split())
graph = [list(map(str,input().strip())) for _ in range(N)]
visited = [ [0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j] == "I":
            start = (i,j)

y,x = start
result = bfs(y,x)
    
print(result if result else "TT")