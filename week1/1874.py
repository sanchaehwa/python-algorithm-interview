import sys
#스택에 Push하는 순서는 반드시 오름차순을 지켜야함
class Solution:
    def stackSequence(self)->None:
        n = int(sys.stdin.readline())
        target = [int(sys.stdin.readline().strip()) for _ in range(n)]
        stack = []
        current = 1
        idx = 0
        result = []
        while idx < n:
            if current <= target[idx]:
                stack.append(current)
                result.append("+")
                current += 1
            else:
                if stack and stack[-1] == target[idx]:
                    stack.pop()
                    result.append("-")
                    idx += 1
                else:
                    print("NO")
                    return
        for r in result:
            print(r)
solution = Solution()
solution.stackSequence()