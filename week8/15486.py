import sys
input = sys.stdin.readline


N = int(input())
dp = [0] * (N+1)
T = list()
P = list()
for _ in range(N):
    t,p = map(int,input().split())
    T.append(t)
    P.append(p)
for j in range(N-1,-1,-1):
    if (j+T[j]) <= N:
        dp[j] = max(dp[j+1],dp[j + T[j]] +P[j]) 
    else:
        dp[j] = dp[j+1]
print(dp[0])
print(dp)