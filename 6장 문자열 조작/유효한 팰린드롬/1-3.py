import re

#슬라이싱 
s = input()
class Solution:
    def isPalindrome(self,s: str) -> bool:#return 반환값 true/false
        s = s.lower()
        s = re.sub('[^a-z0-9]','',s)
        
        return s == s[::-1] #문자열 뒤집은거랑 같은지
sol = Solution()
print(sol.isPalindrome(s))