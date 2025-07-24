import sys
input = sys.stdin.readline

def dfs(y,x):
    #방문처리
    visited[y][x] = True
    #자기 자신을 포함
    count = 1
    #상하좌우 탐색 (대각선은 제외)
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]
    for i in range(4):
        ey = y + dy[i]
        ex = x + dx[i]
        if 0 <= ey < N and 0 <= ex < N:
            if graph[ey][ex] == 1 and not visited[ey][ex]:
                count += dfs(ey,ex)
    return count

N = int(input())
graph = [list(map(int,input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
#집 수 
total = []
for y in range(N):
    for x in range(N):
        if graph[y][x] == 1 and not visited[y][x]:
            total.append(dfs(y,x))
total.sort()
print(len(total))
for i in total:
    print(i)