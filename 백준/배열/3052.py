import collections

class Solution:
    def divisionNumber(self, number:list)->int:
        result = []
        for i in number:
            result.append(i%42)
        count = collections.Counter(result)
        print(len(count))


solution = Solution()
number = [int(input()) for _ in range(10)]
solution.divisionNumber(number)