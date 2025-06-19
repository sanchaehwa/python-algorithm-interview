import sys
class Solution:
    def balancedWorld(self)->None:
        # dot_count = 0
        # while True:
        #     line = sys.stdin.readline().strip()
        #     if line == ".":
        #         dot_count +=1
        #         if dot_count == 2:
        #             break
        #     else:
        #         dot_count = 0
        #     lines.append(line)
        while True:
            a = input()
            stack = []
            if a == ".":
                break
            for i in a:
                if i == "(" or i =="[":
                    stack.append(i)
                elif i == ")":
                    if len(stack) != 0 and stack[-1]== "(": #비어있지않은 경우에 
                        stack.pop() #짝이 맞는경우
                    else:
                        stack.append(')')
                        break
                elif i == "]":
                    if len(stack) != 0 and stack[-1]=="[": 
                        stack.pop()
                    else:
                        stack.append(']')
                        break
            if len(stack) == 0:
                print("yes")
            else:
                print("no")
solution = Solution()
solution.balancedWorld()