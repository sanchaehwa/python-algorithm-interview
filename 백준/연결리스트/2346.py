
from collections import deque

class Solution:
    def balloons(self,n:int,deq:deque)->list:
        answer = []
        while deq:
            idx,now_turn = deq.popleft()
            answer.append(idx+1)
            if now_turn > 0:
                deq.rotate(-(now_turn-1))
            else:#음수
                deq.rotate(-(now_turn))
        return answer


n = int(input())
deq = deque(enumerate(map(int, input().split())))
solution = Solution()
print(*solution.balloons(n,deq))
