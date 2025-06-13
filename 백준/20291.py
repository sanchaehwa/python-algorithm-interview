from collections import Counter
def solution(k:int, nums : list) ->dict:
    file = []
    for i in nums:
        name,extension = i.split('.')
        file.append(extension)
    goal = Counter(file)
    for i,j in sorted(goal.items()):
        print(i,j)

k = int(input())
nums =  [input() for _ in range(k)]
solution(k,nums)