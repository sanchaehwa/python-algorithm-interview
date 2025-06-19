import sys
from collections import deque
class Solution:
    def josephu(self)->None:
        n,m = map(int,sys.stdin.readline().split())
        people = deque(range(1,n+1))
        result = []
        while people:
            people.rotate(-m + 1)
            result.append(people.popleft())
        print("<"+ ", ".join(map(str,result))+">")            
solution = Solution()
solution.josephu()