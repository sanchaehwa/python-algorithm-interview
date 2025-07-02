import sys
from collections import deque
class Solution:
    def zero(self)->int:
        N = int(sys.stdin.readline())
        #재민이가 부른 수 
        num = [int(sys.stdin.readline()) for _ in range(N)]
        #fifo 
        output = deque()
        for i in num:
            if i == 0:
                output.popleft() #최근에 쓴 수 지우기
            else:
                output.appendleft(i)
        print(sum(output))
solution = Solution()
solution.zero()