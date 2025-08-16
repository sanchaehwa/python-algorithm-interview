import sys
input = sys.stdin.readline

N,M = map(int,input().split())
lst = sorted(set(map(int,input().split())))
n = len(lst)
seq = list()

def recur(s,depth):
    if depth == M:
        print(' '.join(map(str,seq)))
    for i in range(s,n):
        seq.append(lst[i])
        recur(i,depth+1)
        seq.pop()
recur(0,0)