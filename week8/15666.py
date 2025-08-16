import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = sorted(set(map(int, input().split())))
n = len(lst)
seq = []

def recur(depth):
    if depth == M:
        print(' '.join(map(str, seq)))
        return
    for j in range(n):
        seq.append(lst[j])
        recur(depth+1)  
        seq.pop()

recur(0)