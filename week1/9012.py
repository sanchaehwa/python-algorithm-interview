import sys
class Solution:
    def parentheses(self) -> None:
        n = int(sys.stdin.readline())
        for _ in range(n):
            stack = []
            text = list(sys.stdin.readline().strip())
            is_valid = True
            for t in text:
                if t == "(":
                    stack.append(t)
                elif t == ")":
                    if stack:
                        stack.pop()
                    else:
                        is_valid = False
                        break
            if is_valid and not stack:
                print("YES")
            else:
                print("NO")

solution = Solution()
solution.parentheses()