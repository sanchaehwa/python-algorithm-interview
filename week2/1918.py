#후위표기식
# (이게 시작 - ) 이게 끝
import sys
class Solution:
    def RPN(self)->str:
        operator = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
        #후위표기식
        expression = sys.stdin.readline().strip()
        stack = [] #연산자를 담을 stack
        result = []
        #Operator에 없으면 피 연산자
        #stack에서 pop 하는기준 1. 우선순위가 같으면 pop 2.) 가 나오면 pop
        for i in expression:
            if i.isalpha(): #피연산자인경우
                result.append(i)
            elif i == "(":
                stack.append(i)
            elif i == ")":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                stack.pop() #( pop
            else:
                while stack and operator[stack[-1]] >= operator[i]:
                    result.append(stack.pop())
                stack.append(i)        
        while stack:
            result.append(stack.pop())
        print(''.join(result))  
solution = Solution()
solution.RPN()

