#3잔 연속으로 마실수는 없다 -> 2 - 1 1 - 2 2 - 2
#dp[i] 
import sys
class Solution:
    def drinkWine(self)->int:
        #포도주 잔의 수 
        n = int(sys.stdin.readline())
        #포도주의 양
        wine = [int(sys.stdin.readline()) for _ in range(n)]
        dp = [0] * 10001 #최대 포도주의양
        #n=1 
        if n == 1:
            print(wine[0])
            return
        #n=2
        if  n == 2:
            print(wine[0]+ wine[1])
            return
        
        dp[0] = wine[0]
        dp[1] = wine[0]+wine[1]
        dp[2] = max(dp[1],wine[0]+ wine[2], wine[1]+wine[2])
        for i in range(3,n):
            dp[i] = max(dp[i-3] + wine[i-1]+wine[i], wine[i] + dp[i-2] ,dp[i-1]) #현재 잔은 마시지않고 이전 최대만 불러옴
        print(dp[n-1])
solution = Solution()
solution.drinkWine()