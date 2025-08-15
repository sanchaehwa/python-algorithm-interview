import sys
import re

class Solution:
    def iCanDoIt(self) -> int:
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
        ops = set('+-*/')
        #식 입력받고
        expression = sys.stdin.readline().strip().replace(' ', '')
        if not expression:
            print("ROCK")
            return
        #정수 및 연산자, 괄호로 토큰 분리
        tokens = re.findall(r'\d+|[()+\-*/]', expression)
        #토큰 확인
        if tokens[0] in ops or tokens[-1] in ops:
            print("ROCK")
            return

        for i in range(len(tokens) - 1):
            cur, nxt = tokens[i], tokens[i + 1]
            if cur in ops and nxt in ops:
                print("ROCK")
                return
            if cur == '(' and (nxt in ops or nxt == ')'):
                print("ROCK")
                return
            if cur in ops and nxt == ')':
                print("ROCK")
                return
            if cur == '(' and nxt == ')':
                print("ROCK")
                return

        s = []
        stack = []
        for token in tokens:
            if token.isdigit():
                s.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    s.append(stack.pop())
                if not stack or stack[-1] != '(':
                    print("ROCK")
                    return
                stack.pop()
            elif token in ops:
                while stack and precedence[stack[-1]] >= precedence[token]:
                    s.append(stack.pop())
                stack.append(token)

        while stack:
            if stack[-1] == '(':
                print("ROCK")
                return
            s.append(stack.pop())

        stack2 = []
        for token in s:
            if token.isdigit():
                stack2.append(int(token))
            elif token in ops:
                if len(stack2) < 2:
                    print("ROCK")
                    return
                b = stack2.pop()
                a = stack2.pop()
                if token == '+':
                    stack2.appegind(a + b)
                elif token == '-':
                    stack2.append(a - b)
                elif token == '*':
                    stack2.append(a * b)
                elif token == '/':
                    if b == 0 or a % b != 0:
                        print("ROCK")
                        return
                    stack2.append(a // b)

        if len(stack2) != 1:
            print("ROCK")
        else:
            print(stack2[0])

solution = Solution()
solution.iCanDoIt()
# s = input()
# new = ''
# check = ''
# num = ['0','1','2','3','4','5','6','7','8','9','(',')']
# if s.count('()') != 0:
#     new += 'x'
# for i in s:
#     if i =='/':
#         new += '//'
#     else:
#         new += i
#     if i not in num:
#         check += '&'
#     else:
#         check+=i

# try:
#     eval(check)
#     print(eval(new))
# except:
#     print("ROCK")