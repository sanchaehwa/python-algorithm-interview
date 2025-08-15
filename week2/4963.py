import sys
sys.setrecursionlimit(10**6)
def dfs(x,y):
    visited[y][x] = True
    dx = [0, 0, 1, -1, -1, -1, 1, 1]
    dy = [-1, 1, 0, 0, -1, 1, -1, 1] 
    for i in range(8):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < w and 0 <= ny < h:
            if graph[ny][nx] == 1 and not visited[ny][nx]:
                dfs(nx,ny)

#지도 너비 w , 높이 h
while True:
    w,h = map(int,sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    graph = []
    for _ in range(h):
        graph.append(list(map(int,input().split())))
    visited = [[False] * w for _ in range(h)]
    cnt = 0
    for y in range(h):
        for x in range(w):
            if graph[y][x] and  visited[y][x] == False:
                dfs(x,y)
                cnt += 1
    print(cnt)
