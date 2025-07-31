import sys
input = sys.stdin.readline

#관찰횟수 
N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]
moved = {}
for l in lst:
    k = l[0]
    v = l[1]
    if k not in moved:
        moved[k] = []
    moved[k].append(v)
cnt = 0
for m in moved:
    cow = moved[m]
    for i in range(len(cow)-1):
        if cow[i] != cow[i+1]:
            cnt += 1
print(cnt)
