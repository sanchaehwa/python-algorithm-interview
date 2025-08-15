import sys
from collections import deque
class Solution:
    def printer(self)->int:
        #테스트 케이스 수 
        t = int(sys.stdin.readline())
        for _ in range(t):
            #문서의 개수 , 0번째로 인쇄된 문서가 궁금
            n,k = map(int,sys.stdin.readline().split())
            paper = list(map(int, sys.stdin.readline().split()))
            q = deque((i,p) for i ,p in enumerate(paper))
            order = 0
            while q:
                max_priority = max(p for _, p in q) #중요도만 뽑아오려고 - 
                if q[0][1] == max_priority:
                    order += 1
                    idx, _ = q.popleft()
                    if idx == k:
                        print(order)
                        break
                else:
                    q.rotate(-1) #뒤로 보냄 : deque의 rotate
solution = Solution()
solution.printer()
