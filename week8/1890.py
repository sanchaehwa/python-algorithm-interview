import sys
input = sys.stdin.readline


N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
dy = [1,0]
dx = [0,1]
result = []
for y in range(N):
    for x in range(N):
        if y == N-1 and x == N-1:
            print(dp[y][x])
        for i in range(2):
            #벡터이기때문에 곱해서 해야해
            ny = y + dy[i] * graph[y][x]
            nx = x + dx[i] * graph[y][x]
            if 0 <= ny < N and 0 <= nx < N:
                #값을 누적해야함!
                dp[ny][nx] += dp[y][x]
