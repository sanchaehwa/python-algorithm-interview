def solution(nums):
    max_number = max(nums)
    index = nums.index(max_number)
    print(max_number)
    print(index+1)


nums = [int(input()) for _ in range(9)]
solution(nums)