class Solution():
    def trap(self, height: list[int]) -> int:
        stack = []
        volumn = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:   #변곡점
                top = stack.pop()
                if not stack:
                    break
                distance = i - stack[-1] -1
                waters = min(height[i],height[stack[-1]]) - height[top]
                volumn += distance * waters
            stack.append(i)
        return volumn

height = list(map(int, input().split()))
solution = Solution()
print(solution.trap(height))