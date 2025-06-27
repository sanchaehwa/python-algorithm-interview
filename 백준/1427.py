import sys

class Solution:
    def sortInside(self):
        N = list(map(str,sys.stdin.readline().strip()))
        N.sort(reverse=True)
        print(''.join(N))
solution = Solution()
solution.sortInside()