class Solution():
    def arrayPairSum(self,nums:list[int])->int:
        sum = 0
        pair = []
        #오름차순 정렬
        #nums.sort()
        #내림차순 정렬
        nums.sort(reverse=True)
        for i in nums:
            pair.append(i)
            if len(pair) == 2:
                sum  += min(pair)
                pair=[]
        return sum
    
nums = list(map(int, input().split()))
solution = Solution()
print(solution.arrayPairSum(nums))