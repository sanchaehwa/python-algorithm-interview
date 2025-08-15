#dp문제 - ~ 1이되는 최소 횟수
import sys
class Solution:
    def makeOne(self) -> int:
        #주어지는 수
        N = int(sys.stdin.readline())
        dp = [0,0,1,1] #0은 인덱스를 맞추고 1 ~ 3까지는 하드코딩 2,3으로 나눌수없으면 -1 , 2,3으로 나눌수있으면 나눈 몫
        for i in range(4,N+1):
            dp.append(dp[i-1]+1) 
            if i % 2 == 0:
                dp[i] = min(dp[i],dp[i//2]+1)
            if i % 3 == 0:
                dp[i] = min(dp[i],dp[i//3]+1)
        print(dp[N])
solution = Solution()
solution.makeOne()