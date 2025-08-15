import sys
class Solution:
    def RGB(self)->int:
        N = int(sys.stdin.readline())
        graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
        dp = [[0] * 3 for _ in range(N)]
        dp[0] = graph[0] #26 , 40 , 83
        for i in range(1,N):
            dp[i][0] = min(dp[i-1][1],dp[i-1][2])  + graph[i][0] # G --- B 
            dp[i][1] = min(dp[i-1][0],dp[i-1][2]) + graph[i][1] #R -- B
            dp[i][2] = min(dp[i-1][0],dp[i-1][1]) + graph[i][2] #R -- G
        print(min(dp[-1]))
            

solution = Solution()
solution.RGB()