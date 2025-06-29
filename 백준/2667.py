import sys
sys.setrecursionlimit(10**6)  # 재귀 한도 설정

def dfs(x,y):
    visited[x][y] = True
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    count = 1 #자기 자신도 포함
    for i in range(4):
        nx,ny = dx[i] + x,dy[i] + y
        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny]==1 and not visited[nx][ny]:
                count += (dfs(nx,ny))
    return count

#지도의 크기(정사각형)
N = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
#1 상하좌우에 1이없으면 탐색 끝으로?
result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] and not visited[i][j]:
            result.append(dfs(i,j))
print(len(result))
for r in sorted(result):
    print(r)