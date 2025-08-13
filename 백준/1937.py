import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


dy = [-1,1,0,0]
dx = [0,0,1,-1]
def dfs(y,x):
    if dp[y][x] != -1:
        return dp[y][x]
    dp[y][x] = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if graph[ny][nx] > graph[y][x]:
                dp[y][x] = max(dp[y][x],dfs(ny,nx)+1)
    return dp[y][x]
                


N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
dp = [[-1] * N for _ in range(N)]
answer = 0
#출발점을 찾아야하는데
for y in range(N):
    for x in range(N):
        answer = max(answer,dfs(y,x))
print(answer)