import sys
class Solution:
    def searchDoc(self):
        doc = sys.stdin.readline().strip()
        search = sys.stdin.readline().strip()
        start = 0
        cnt = 0
        l = len(search)
        d = len(doc)
        while start <= d - l:
            if doc[start:start+l] == search:
                cnt += 1
                start += l
            else:
                start += 1
        print(cnt)

solution = Solution()
solution.searchDoc()