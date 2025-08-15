import sys
from collections import deque

class Solution:
    def deque2(self)->None:
        #명령의 수 
        N = int(sys.stdin.readline())
        dq = deque()
        for _ in range(N):
            command = list(sys.stdin.readline().split())
            c1 = command[0]
            v1 = command[1] if len(command) == 2 else None

            #정수 x를 덱 앞에 넣는다
            if c1 == '1':
                dq.appendleft(v1)
            elif c1 == '2': #덱 뒤에 넣는다
                dq.append(v1)
            elif c1 == '3':
                if dq:
                    print(dq.popleft())
                else:
                    print(-1)
            elif c1 == '4':
                if dq:
                    print(dq.pop())
                else:
                    print(-1)
            elif c1 == '5':
                print(len(dq))
            elif c1 == '6':
                if dq:
                    print(0)
                else:
                    print(1)
            elif c1 == '7':
                if dq:
                    print(dq[0])
                else:
                    print(-1)
            elif c1 == '8':
                if dq:
                    print(dq[-1])
                else:
                    print(-1)
solution = Solution()
solution.deque2()