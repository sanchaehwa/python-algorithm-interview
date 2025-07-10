import sys
class Solution:
    def LCS(self)->int:
        A = sys.stdin.readline().strip()
        B = sys.stdin.readline().strip()
        #A.B
        dp = [[0] * (len(B)+1) for _ in range(len(A)+1)]
        for i in range(1,len(A)+1): #끝까지 탐색하기위해서 +1
            for j in range(1,len(B)+1): 
                if A[i-1] == B[j-1]: #이전값으로 비교 - 점진
                    dp[i][j] = dp[i-1][j-1] + 1
                else: #다르면 위, 왼쪽 최대값
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        #print(dp[-1][-1])
        print(dp[len(A)][len(B)])
solution = Solution()
solution.LCS()