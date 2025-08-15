#파이썬 다운 방식
#인덱스 슬라이싱
class Solution():
    def arrayPairSum(self, nums:list[int]) -> int:
        nums.sort()
        return sum(nums[::2]) #2칸씩 건너뛰기 == 짝수인덱스만 
        #return sum(sorted(nums)[::2])
    
nums = list(map(int, input().split()))
solution = Solution()
print(solution.arrayPairSum(nums))