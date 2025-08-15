'''
dp[0] = 1
dp[1] = 1
dp[2] = 2

1. An-2 > An => 성립하면 dp[n-2] +1 
2. An-1 > An => 성립하면 dp[n-1] +1
3. dp 리스트 에서 최대인 값이 이제 -> 가장 긴 감소하는 수열의 길이 

'''
import sys
input = sys.stdin.readline
N = int(input()) 
dp = [1] * N #LDS 길이 초기화 -> 고정값을 넣고 그이후부터 append 하지않는건 N의 값이 고정되어 있는게 아니기때문
lst = list(map(int,input().split()))
for i in range(N):
    for j in range(i):
        if lst[j] > lst[i]:
            dp[i] = max(dp[i],dp[j]+1)
        
print(max(dp))


