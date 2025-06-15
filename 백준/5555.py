#N개의 반지, 문자열 시작과 끝 연결 - 반지 + 반지
#입력 2+N
class Solution:
    def ring(self,target:str,n:int,rings:list)->int:
        cnt = 0
        for i in rings:
            if target in i:
                cnt += 1
        print(cnt)



target = input()
n = int(input())
rings=[]
for _ in range(n):
    w = input()
    rings.append(w+w)
solution = Solution()
solution.ring(target,n,rings)