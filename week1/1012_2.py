import sys
sys.setrecursionlimit(10**6)

def dfs(x,y):
    #방문처리
    visited[x][y] = True
    #상하좌우 (-1,0) (1,0) (0,1), (0,-1)
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0 <= ny < m:
            #재귀호출
            if graph[nx][ny] == 1 and not visited[nx][ny]: #방문하지 않은 경우
                dfs(nx,ny)

t = int(sys.stdin.readline())
for _ in range(t):
    m,n,k = map(int,sys.stdin.readline().split())
    graph = [[0] * m for _ in range(n)]
    #방문 여부
    visited = [[False] * m for _ in range(n)]
    for _ in range(k):
        x,y = map(int,sys.stdin.readline().split())
        #해당 위치에 배추 심어주기
        graph[y][x] = 1
    #배추 개수
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] and visited[i][j] == False:
                dfs(i,j)
                cnt += 1
    print(cnt)
