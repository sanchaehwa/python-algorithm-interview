import sys
input = sys.stdin.readline

N = int(input()) #민규가 N개의 카드를 갖어야함
card =[0] + list(map(int,input().split()))
dp = [0] * (N+1)
for i in range(1,N+1):
    for j in range(1,i+1):
        dp[i] = max(dp[i-j] + card[j] , dp[i])
print(dp[N])