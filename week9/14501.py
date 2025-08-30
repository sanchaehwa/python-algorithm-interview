import sys
input = sys.stdin.readline

N = int(input())
time = [0]
money = [0]

for _ in range(1,N+1):
    t,m = map(int,input().split())
    time.append(t)
    money.append(m)

dp = [0] * (N+2)
for i in range(N,0,-1):
    if i + time[i] <= N+1:
        dp[i] = max(dp[i+1] , money[i] + dp[i+time[i]])
    else:
        dp[i] = dp[i+1]
print(dp[1])

        