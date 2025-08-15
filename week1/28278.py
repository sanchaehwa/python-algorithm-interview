#1 : 정수 x를 스택에 넣음
#2 : 스택에 정수가 있으면, 위에 정수빼고 출력 - 없으면 -1
#3 : 스택에 들어있는 정수의 개수
#4 : 스택 비어있으면 1 , 아니면 0
#5 : 스택 있으면 위의 정수 출력, 없으면 -1 
import sys

class Solution:
    def stack2(self) -> None:
        stack = []
        n = int(input())

        for _ in range(n):
            command = sys.stdin.readline().split()
            cmd = command[0]

            if cmd == "1":
                stack.append(int(command[1]))
            elif cmd == "2":
                if stack:
                    print(stack.pop())
                else:
                    print(-1)
            elif cmd == "3":
                print(len(stack))
            elif cmd == "4":
                print(1 if not stack else 0)
            elif cmd == "5":
                if stack:
                    print(stack[-1])
                else:
                    print(-1)

solution = Solution()
solution.stack2()