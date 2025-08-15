import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
n = N//2
lst = list(combinations(range(N),n))
s = len(lst) // 2
lst1 = lst[:s] #앞 절반 
lst2 = lst[s:]#뒷 절반
lst2 = lst2[::-1]

answer = int(1e9) #최대값으로 
for i in range(s):
    start_team = lst1[i]
    link_team = lst2[i]
    start = 0
    for x in start_team:
        for y in start_team:
            if x != y:
                start += graph[x][y]
    link = 0
    for x in link_team:
        for y in link_team:
            if x != y:
                link += graph[x][y]
    answer = min(answer, abs(start-link))

print(answer)
