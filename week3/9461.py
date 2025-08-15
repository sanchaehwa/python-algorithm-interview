import sys
class Solution:
    def waveSequence(self)->None:
        T = int(sys.stdin.readline())
        result = []
        for i in range(T):
            N = int(sys.stdin.readline())
            if N <= 3:
                result.append(1)
                continue
            dp = [0] * (N+1)
            dp[1] = dp[2] = dp[3] = 1
            for j in range(4,N+1):
                dp[j] = dp[j-3] + dp[j-2]
            result.append(max(dp))
        for i in result:
            print(i)
solution = Solution()
solution.waveSequence()

