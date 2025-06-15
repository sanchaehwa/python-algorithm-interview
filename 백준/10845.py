#Queue 구현 방법 : list, queue
from collections import deque
import sys

class Solution:
    def queue1(self)->int:
        #정수 x를 큐에 넣는 연산
        queue = deque()
        input = sys.stdin.readline
        n = int(input())
        for _ in range(n):
            command = input().split()
            cmd =command[0]
            #1. 정수 x를 큐에 넣는 연산
            if cmd == "push":
                queue.append(int(command[1]))
            #2. 큐에서 가장 앞에 있는 정수 빼고, 그 수를 출력 : pop
            #  FIFO 구조라서 get하면 첫번째 요소 제거 (왼쪽)
            elif cmd == "pop":
                print(queue.popleft() if queue else -1)
            elif cmd == "size":
                print(len(queue))
            elif cmd == "empty":
                print(1 if not queue else 0)
            elif cmd == "front":
                print(queue[0] if queue else -1)
            elif cmd == "back":
                print(queue[-1] if queue else -1)
solution = Solution()
solution.queue1()

#front - back : 양방향 deque