import sys
class Solution:
    def lis1(self)->int:
        N = int(sys.stdin.readline())
        num = list(map(int,sys.stdin.readline().split()))
        dp = [1] * N #자기 자신 하나로 LIS 가 가능해서 1
        for i in range(0,N):
            for j in range(i):
                if num[j] < num[i]:#이전원소보다 크면 부분수열이 되니깐
                    dp[i] = max(dp[i],dp[j]+1) #이전 원소까지의 수열 길이 += 현재 수열의 길이 (자기자신) 
        print(max(dp))
solution = Solution()
solution.lis1()
