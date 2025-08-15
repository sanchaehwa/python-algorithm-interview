import sys
from collections import deque
class Solution:
    def queue2(self)->None:
        N = int(sys.stdin.readline())
        queue = deque()
        for _ in range(N):
            command = list(sys.stdin.readline().strip().split())
            c1 = command[0]
            v1 = int(command[1]) if len(command) == 2 else None
            if c1 == "push":
                queue.append(v1)
            elif c1 == "pop":
                if queue:
                    print(queue.popleft())
                else:
                    print(-1)
            elif c1 == "size":
                print(len(queue))
            elif c1 == "empty":
                if not queue:
                    print(1)
                else:
                    print(0)
            elif c1 == "front":
                if queue:
                    print(queue[0])
                else:
                    print(-1)
            elif c1 == "back":
                if queue:
                    print(queue[-1])
                else:
                    print(-1)
solution = Solution()
solution.queue2()