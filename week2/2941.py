import sys
class Solution:
    def croatia(self,a:str)->int:
        croatiaList = ["c=","c-","dz=","d-","lj","nj","s=","z="]
        for i in croatiaList:
            a = a.replace(i,"!") #하나의 문자로 
        print(len(a))
        

a = sys.stdin.readline().strip()
solution = Solution()
solution.croatia(a)

