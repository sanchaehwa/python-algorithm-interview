import sys
class Solution:
    def triangle(self)->int:
        #삼각형의 크기
        N = int(sys.stdin.readline())
        graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
        dp = [[0] * N for _ in range(N)]
        dp[N-1] = graph[N-1]
        for i in range(N-2,-1,-1):
            for j in range(len(graph[i])):
                dp[i][j] = max(dp[i+1][j+1],dp[i+1][j]) + graph[i][j]
        print(dp[0][0])
solution = Solution()
solution.triangle()