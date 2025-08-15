import sys

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        min_price = sys.maxsize
        for i in prices:
            min_price = min(min_price,i)
            profit = max(profit , i - min_price)
        return profit

prices = list(map(int, input().split()))
solution = Solution()
print(solution.maxProfit(prices))