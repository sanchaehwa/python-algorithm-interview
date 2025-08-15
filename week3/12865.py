import sys

class Solution:
    def ordinaryBackpack(self)->int:
        N,K = map(int,sys.stdin.readline().split())
        bag = [list(map(int,sys.stdin.readline().split())) for _ in range(N)] 
        #[[6,13] , [4,8] , [3,6] , [5,12]]
        dp = [[0] * (K+1) for _ in range(N+1)]
        for i in range(1,N+1):
            for j in range(1,K+1):
                if j >= bag[i-1][0]: 
                    dp[i][j] = max(bag[i-1][1] +dp[i-1][j-bag[i-1][0]],dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]

        print(dp[N][K])
solution = Solution()
solution.ordinaryBackpack()