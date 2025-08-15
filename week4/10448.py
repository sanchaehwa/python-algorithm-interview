import sys
from itertools import combinations
N = int(sys.stdin.readline())
# num = [int(sys.stdin.readline()) for _ in range(N)]
tri = [i * (i + 1) // 2 for i in range(1, 46)]
for _ in range(N):
    num = int(sys.stdin.readline())
    found = False
    for i in tri:
        for j in tri:
            for l in tri:
                if i + j + l == num:
                    found = True
                    break
            if found:
                break
        if found:
            break
    print(1 if found else 0)
                    
    # for j in range(1,46): #1000 이하의 삼각수
    #     k = j * (j+1)//2
    #     if k <= num:
    #         lst.append(k)
    # find = list(combinations(lst,3))
    # for k in find:
    #     if sum(k) == num:
    #         result.append(k)
    # if len(result) == 0:
    #     print(0)
    # else:
    #     print(1)
