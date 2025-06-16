import sys
#스택
class Solution:
    def keyLogger(self)->str:
        n = int(sys.stdin.readline())
        for _ in range(n):
            l_stack = []
            r_stack = []
            password = sys.stdin.readline().rstrip()
            for pw in password:
                if pw == "<": #왼쪽 -> 오른
                    if l_stack:
                        r_stack.append(l_stack.pop())
                elif pw == ">": #오른 -> 왼쪽
                    if r_stack:
                        l_stack.append(r_stack.pop())
                elif pw == "-": #커서바로앞에 문자 삭제 - 왼쪽
                    if l_stack:
                        l_stack.pop()
                else:
                    l_stack.append(pw)
            l_stack.extend(reversed(r_stack))
            print("".join(l_stack))
                                            
solution = Solution()
solution.keyLogger()