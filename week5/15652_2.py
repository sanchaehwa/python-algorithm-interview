import sys
input = sys.stdin.readline

#방문여부는 측정할 필요가 없음
N,M = map(int,input().split())
rs = []

def recur(start,depth):
    if depth == M:
        print(' '.join(map(str,rs)))
        return
    for i in range(start,N+1):
        rs.append(i)
        recur(i,depth+1) 
        rs.pop()
recur(1,0)
