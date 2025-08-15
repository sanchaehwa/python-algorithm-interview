#dict : 시간복잡도 O(1)
class Solution():
    def twoSum(self,nums:list[int],target:int)->list[int]:
        #nums 딕셔너리로 변환
        nums_map = {}
        # for i,num in enumerate(nums):
        #     nums_map[num] = i
        #key 값을 target 에서 빼서 그 수를 키값으로 찾으면 됨

        for i,num in enumerate(nums):
            if target-num in nums_map:
                # i = dict : value nums: index , num = dict:key nums:value
                return [nums_map[target-num],i]
            nums_map[num] = i

nums = list(map(int,input().split()))
target = int(input())
solution = Solution()
print(solution.twoSum(nums,target))