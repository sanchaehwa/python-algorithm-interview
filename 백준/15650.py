import sys
input = sys.stdin.readline

N,M = map(int,input().split()) #M은 깊이
rs = []
chk = [False] * (N+1)

def recur(start,depth):
    if depth == M:
        print(' '.join(map(str,rs)))
        return
    for i in range(start,N+1):
        if not chk[i]:
            chk[i] = True
            rs.append(i)
            recur(i+1, depth+1)
            chk[i] = False
            rs.pop()
recur(1,0)