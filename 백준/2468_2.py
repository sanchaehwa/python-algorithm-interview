import sys
from collections import deque
input = sys.stdin.readline
#행과 열의 개수 == N이하 높이는 물의잠김
def bfs(y,x,height):
    q = deque()
    q.append((y,x))
    while q:
        ey,ex = q.popleft()
        dy = [-1,1,0,0]
        dx = [0,0,1,-1]
        for i in range(4):
            ny = dy[i] + ey
            nx = dx[i] + ex
            if 0 <= ny < N and 0 <= nx < N:
                if not visited[ny][nx] and graph[ny][nx] >= height:
                    q.append((ny,nx))
                    visited[ny][nx] = True

#기준 높이가 6일때, 7일때 최대개수를 구해야하는거니깐
# N * N
N = int(input())
#아무것도 입력하지않는경우
if N == 0:
    print(0)
    exit()
graph = [list(map(int,input().split())) for _ in range(N)]
result = []
max_height = max(map(max,graph))
for h in range(0,max_height+1):
    height = h
    visited = [[False] * N for _ in range(N)]
    cnt =0
    for y in range(N):
        for x in range(N):
            if not visited[y][x] and graph[y][x] >= height:
                bfs(y,x,height)
                cnt +=1
    result.append(cnt)
print(max(result))
