class Solution():
    def arrayPairSum(self, nums:list[int]) -> int:
        sum = 0
        nums.sort()
        for idx,i in enumerate(nums):
            if idx % 2 == 0:
                sum += i
        return sum
    
nums = list(map(int, input().split()))
solution = Solution()
print(solution.arrayPairSum(nums))