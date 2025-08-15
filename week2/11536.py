import sys
class Solution:
    def inLine(self)->str:
        N = int(sys.stdin.readline())
        name = [sys.stdin.readline().strip()for _ in range(N)]
        t1 = sorted(name,reverse=True)
        t2 = sorted(name)
        if name == t1:
            print("DECREASING")
        elif name == t2:
            print("INCREASING")
        elif name != t1 and name != t2:
            print("NEITHER")
solution = Solution()
solution.inLine()

