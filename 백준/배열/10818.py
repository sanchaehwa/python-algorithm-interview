def solution(x,nums):
    answer = []
    nums.sort()
    answer.append(nums[0])
    answer.append(nums[-1])
    for j in range(len(answer)):
        print(answer[j], end=' 5')
# 몇개를 입력받을지 
x = int(input())
# X개 만큼 입력받아서,배열
nums = [*map(int,input().split())]
print(solution(x,nums))