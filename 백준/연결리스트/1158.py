from collections import deque
class Solution:
    def josephus(self,k:list)->list:
        n,idx = k[0],k[1]
        numbers = [i for i in range(1,n+1)]
        result = []
        num = 0 
        for _ in range(n):
            num += idx-1
            if num >= len(numbers):
                num = num % len(numbers)
            result.append(str(numbers.pop(num)))
            
        print("<"+", ".join(result)[:],">",sep='')


k = list(map(int,input().split()))
solution = Solution()
print(solution.josephus(k))


