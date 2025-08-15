import sys
input = sys.stdin.readline

N = int(input())
if N == 1: 
    print(1)
    exit()
#앞의자리가 0이면 이친수 아님 - 1이면 이친수임
dp = [[0] * 2 for _ in range(N+1)]
#초기값 
dp[1][0] = 0
dp[1][1] = 1 #앞 자리가 1이어야하고
for i in range(2,N+1):
    dp[i][0] = dp[i-1][0] + dp[i-1][1]
    dp[i][1] = dp[i-1][0]
print(dp[N][1] + dp[N][0])

