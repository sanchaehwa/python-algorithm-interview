#브루트 포스 : 무차별 대입(모든 조합을 더해서 일일이 확인해보는)O(n^2)

class Solution:
    def twoSum(self,nums:list[int],target:int)->list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
                
#1차원 배열 입력받기
nums = list(map(int,input().split())) #[2,7,11,15]
target = int(input())
solution = Solution()
print(solution.twoSum(nums,target))