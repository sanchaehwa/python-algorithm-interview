import sys
from collections import deque
class Solution:
    def dokidoki(self)->str:
        student = int(sys.stdin.readline())
        #앞에서부터 뒤순서
        number_ticket = list(map(int,sys.stdin.readline().split()))
        stack = []
        next = 1
        for num in number_ticket:
            while stack and stack[-1] == next:
                stack.pop() #간식
                next += 1
            if num == next:
                next += 1
            else:
                stack.append(num)
        while stack and stack[-1] == next:
            stack.pop()
            next += 1
        if stack:
            print("Sad")
        else:
            print("Nice")
solution = Solution()
solution.dokidoki()