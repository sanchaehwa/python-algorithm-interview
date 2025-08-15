import sys
input = sys.stdin.readline

N,M = map(int,input().split())
visited = [False] * (N+1)
rs = []
def recur(num):
    if num == M:
        print(' '.join(map(str,rs)))
        return
    for i in range(1,N+1):
        rs.append(i)
        recur(num + 1)
        rs.pop()
recur(0)
