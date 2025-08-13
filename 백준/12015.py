'''
현재 수가 더 크면 + 1
'''
import sys
import bisect
input = sys.stdin.readline

N = int(input())
lst = list(map(int,input().split()))
tails = []


for i in lst:
    # for j in range(i):
    #     if lst[j] < lst[i]:
    #         dp[i] = max(dp[i],dp[j]+1)
    idx = bisect.bisect_left(tails,i)
    if idx == len(tails):
        tails.append(i)
    else:
        tails[idx] = i
    print(tails)
print(len(tails))