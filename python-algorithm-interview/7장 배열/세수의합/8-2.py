class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        #정렬
        nums.sort()
        for i in range(len(nums)-2):
            #중복검사
            if i > 0 and nums[i]==nums[i-1]:
                continue
            #다중 할당
            left , right = i + 1, len(nums) -1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while right > left and nums[right] == nums[right-1]:
                        right -=1
                    left += 1
                    right -= 1
        return result
nums = list(map(int, input().split()))
solution = Solution()
print(solution.threeSum(nums))