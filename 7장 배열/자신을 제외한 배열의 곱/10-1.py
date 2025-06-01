class Solution():
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # 오른쪽부터 곱해
        out = []
        p = 1
        for i in range(0,len(nums)):
            out.append(p) # 1 , a , a*b, a*b*c
            p = p * nums[i]
        p =1
        for i in range(len(nums)-1,0-1,-1): #한칸씩 역순 이동
            out[i] = out[i] * p
            p = p * nums[i]
        return out

nums = list(map(int, input().split()))
solution = Solution()
print(solution.productExceptSelf(nums))
