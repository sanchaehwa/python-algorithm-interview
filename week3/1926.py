import sys
sys.setrecursionlimit(10**6)
 
def dfs(x,y):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    cnt = 1 #넓이 
    visited[y][x] = 1
    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if 0<= x1 < m and 0<= y1 < n:
            if not visited[y1][x1] and picture[y1][x1] == 1:
                cnt += dfs(x1,y1)
    return cnt

#세로 -- 가로
n,m = map(int,sys.stdin.readline().split())

picture = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
count = []
for y in range(n):
    for x in range(m):
        if visited[y][x] == 0 and picture[y][x] == 1:
            count.append(dfs(x,y))
if len(count) == 0:
    print(len(count))
    print(0)
else:
    print(len(count))
    print(max(count))