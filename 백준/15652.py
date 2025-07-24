import sys
input = sys.stdin.readline

rs = []
N,M = map(int,input().split())
def recur(start,depth):
    if depth == M:
        print(' '.join(map(str,rs)))
        return
    for i in range(start,N+1):
        rs.append(i)
        recur(i,depth+1)
        rs.pop()
recur(1, 0)