import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

dy = [-1,1,0,0]
dx = [0,0,1,-1]

def dfs(y,x):
    if y == M-1 and x == N-1:
        return 1 
    if dp[y][x] != -1: #이미 처리한 결과
        return dp[y][x] #해당 위치의 dp값
    dp[y][x] = 0 #초기화
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < M and 0 <= nx < N:
            if graph[ny][nx] < graph[y][x]:
                dp[y][x] += dfs(ny,nx)
    return dp[y][x]

# M : 세로 / N: 가로
M,N = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)] #해당 지점에서 목표지점까지 갈수 있는 경로의 수
print(dfs(0,0))