#브루트 포스로 계산
class Solution():
    def threeSum(self,nums:list[int]) -> list[list[int]]:
        results = []
        nums.sort
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i -1]:
                continue
            for j in range(i+1, len(nums)-1):
                if j > i +1 and nums[j] == nums[j-1]:
                    continue
                for k in range(j+1, len(nums)):
                    if k>j+1 and nums[k] == nums[k-1]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        results.append([nums[i],nums[j],nums[k]])
        return results
nums = list(map(int, input().split()))
solution = Solution()
print(solution.threeSum(nums))