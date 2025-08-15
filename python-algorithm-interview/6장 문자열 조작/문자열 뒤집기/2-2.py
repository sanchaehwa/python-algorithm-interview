#문자열 뒤집기 -> reverse
from typing import List
import ast

class Solution():
    def reverseString(self, s: List[str]) -> None: 
        left, right = 0, len(s)-1
        while (left < right):
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1
#문자열 입력
s = ast.literal_eval(input())
solution = Solution()
solution.reverseString(s)
print(s)