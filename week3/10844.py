import sys
class Solution:
    def easyStairsNumber(self)->int:
        #자리수 입력
        N = int(sys.stdin.readline())
        dp =[[0] * 10  for _ in range(N+1)]
        for i in range(1,10):
            dp[1][i]= 1
        mod =  1000000000
        for N in range(2,N+1):
            for i in range(0,10):
                if i == 0:
                    dp[N][0] = dp[N-1][1] 
                elif i == 9:
                    dp[N][i] = dp[N-1][8]
                else:
                    dp[N][i] = dp[N-1][i-1] + dp[N-1][i+1]
        print(sum(dp[N])% mod)
solution = Solution()
solution.easyStairsNumber()            x