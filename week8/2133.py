import sys
input = sys.stdin.readline

N = int(input())
k = 3 * N
dp = [0] * (k+1)

dp[0] = 0 

for i in range(1,3):
    for j in range(i,k+1):
        dp[j] = dp[j-i] +1
print(dp[k])
