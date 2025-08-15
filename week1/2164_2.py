import sys
from collections import deque
#제일 위에 있는 카드 (First IN) -- 아래로 (First Out) => 큐 사용하는 문제
class Solution:
    def card2(self)->int:
        #N개의 카드 
        n = int(sys.stdin.readline())
        #입력값 검증
        if n<=0:
            return -1
        #Queue 
        queue = deque(range(1,n+1))
        while len(queue) > 1: #Queue에 하나가 남을때까지 반복
            queue.popleft() #제일 위에 있는 카드를 버려
            queue.append(queue.popleft())#그 다음 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮기고
        return queue[0]
solution = Solution()
print(solution.card2())
