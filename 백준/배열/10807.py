def solution(n:int,nums:list,k:int)->int:
    return nums.count(k)


n = int(input())
nums = list(map(int, input().split()))
k = int(input())


print(solution(n,nums,k))