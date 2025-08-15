#in을 활용한

class Solution():
    def twoSum(self,nums:list[int],target:int)->list[int]:
            for i,n in enumerate(nums):
                print(i,n)
                print(nums[i+1])
                #i는 인덱스, number는 인덱스의 숫자
                complement = target - n
                #nums[i+1:] n 나머지 수의 배열 (원래 배열의 인덱스 == index(complement)+(i_1) )
                if complement in nums[i+1:]: #일때 반환을 시켜고 함수 종료
                    return([i, nums[i+1:].index(complement)+(i+1)])


#일차원 배열 입력
nums = list(map(int,input().split()))
target = int(input())
solution = Solution()
print(solution.twoSum(nums,target))