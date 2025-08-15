import sys
from itertools import combinations
input = sys.stdin.readline

N,M = map(int,input().split())
nums = list(map(int,input().split()))
cnt = 0
#부분 수열을 담을
for i in range(1,N+1):
    comb = combinations(nums,i)
    for x in comb:
        if sum(x) == M:
            cnt +=1
print(cnt)
