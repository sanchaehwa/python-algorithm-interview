import sys
'''
주어진 자연수 N / 제곱수들의 합으로표현 , 그 항의 최소 개수
'''
input = sys.stdin.readline


N = int(input())


dp = [0] * (N+1)
dp[0] = 0

for i in range(1,N+1):
    dp[i] = i

for i in range(1,N+1):
    for j in range(1,int(i ** 0.5) + 1):
        if i >= j * j:
            dp[i] = min(dp[i],dp[i-j*j]+1)
print(dp[N])