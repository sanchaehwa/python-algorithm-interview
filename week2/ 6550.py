import sys
class Solution:
    def substring(self)->None:
        while True:
            ch = list(sys.stdin.readline().split())
            if len(ch) == 0:
                break #아무입력이없느거
            s = ch[0]
            t = ch[1]
            i = 0
            j = 0
            while len(s) > i and j < len(t):
                if s[i] == t[j]:
                    i += 1
                j += 1
            if len(s) == i:
                print("Yes")
            else:
                print("No")
        
solution = Solution()
solution.substring()