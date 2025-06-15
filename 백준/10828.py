import sys
class Solution:
    def stack1(self)->None:
        stack = []
        for _ in range(int(input())):
            command = sys.stdin.readline().split()
            task = command[0]
            if task == "push":
                stack.append(int(command[1]))
            elif task == "pop": #LIFO 
                print(stack.pop() if stack else -1)
            elif task == "size":
                print(len(stack))
            elif task == "empty":
                print(1 if len(stack)==0 else 0)
            elif task == "top":
                print(stack[-1] if stack else -1)
solution = Solution()
solution.stack1()