import sys
input = sys.stdin.readline

#동전 종류 수 / 만들어야하는 수
n,k = map(int,input().split())
#동전 종류 lst
coin = sorted([int(input().strip()) for _ in range(n)])

dp = [0] * (k+1)

dp[0] = 1 #하나의 동전으로 만들 수 있는 경우의수 *아무것도 선택하지않았을때

for c in coin:
    for i in range(c,k+1):
        dp[i] += dp[i-c]
print(dp[k])