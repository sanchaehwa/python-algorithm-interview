import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coins = sorted([int(input().strip()) for _ in range(n)])
INF = 1e9
dp = [INF] * (k+1)

#아무것도 선택하지않은 경우의수 최소
dp[0] = 0

for c in coins:
    for i in range(c,k+1):
        dp[i] = min(dp[i],dp[i-c]+1) 
print(dp[k] if dp[k] != INF else -1)
