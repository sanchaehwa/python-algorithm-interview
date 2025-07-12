'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''
import sys
input = sys.stdin.readline
cnt = 0
def dfs(y,x):
    #전역변수 사용
    global cnt
    cnt += 1
    visited[y][x] = 1  #방문 처리

    dx = [0,0,1,-1]
    dy = [-1,1,0,0]
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < N and 0 <= ny < N:
            if graph[ny][nx] == 1 and visited[ny][nx] == 0:
                dfs(ny,nx)
    return cnt

N = int(input())
graph = [list(map(int,input().strip())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
home = 0
result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == 0:
            cnt = 0
            home +=1
            result.append(dfs(i,j))
print(home)
result.sort() #오름차순
for i in result:
    print(i)