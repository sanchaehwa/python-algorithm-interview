import sys
from itertools import combinations

input = sys.stdin.readline


N = int(input())
# lst = []
# for i in range(10000000):
#     digits = list(map(int,str(i)))
#     for d in range(len(digits)-1):
#         if digits[d] < digits[d+1]:
#             return
#     lst.append(i)
#     if len(lst) == N-1:
#         print(lst[-1])
answer = []
for i in range(1,11): #1부터 10
    for j in list(combinations(range(10),i)):
        #j는 1,0 2,0 --0 , 2 증가하는 형태
        decrease_Number = ""
        for k in sorted(j,reverse=True):
            decrease_Number += str(k)
        answer.append(int(decrease_Number))
answer.sort()

if(N >= len(answer)):
    print(-1)
else:
    print(answer[N])
