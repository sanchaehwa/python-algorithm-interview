class Solution():
    def maxNumber(self,number:list):
        result = [max(i) for i in number]
        maxNumber = max(result)
        where = [(k+1,m+1) for k in range(9) for m in range(9) if number[k][m] == maxNumber]


        print(maxNumber)
        print(*where[0]) #[()] - 5 7 


number = []
for _ in range(9):
    row = list(map(int,input().split()))
    number.append(row)
solution = Solution()
solution.maxNumber(number)