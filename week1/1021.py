from collections import deque
class Solution:
    def rotateQueue(self,number:list,list_2:list)->int:
        n = number[0]
        q = deque(range(1,n+1))
        cnt = 0
        for i in list_2:
            find_index = q.index(i) #현재위치
            if find_index <= len(q) // 2:
                q.rotate(-find_index)
                cnt += find_index
            else:
                q.rotate(len(q)-find_index)
                cnt += len(q) - find_index
            q.popleft()#맨앞에서 제거
        print(cnt)

number = list(map(int,input().split()))
list_2 = list(map(int,input().split()))
solution = Solution()
solution.rotateQueue(number,list_2)
