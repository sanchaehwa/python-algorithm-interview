import sys
class Solution:
    def LCS(self)->int:
        A = list(sys.stdin.readline().strip())
        B = list(sys.stdin.readline().strip())
        #A.B
        dp = [[0] * (len(B)+1) for _ in range(len(A)+1)]

        print(dp)
        for i in range(len(A)):
            for j in range(len(B)):
                pass
solution = Solution()
solution.LCS()