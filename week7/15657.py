'''
1. 중복 허용
2. 고른 수열은 비 내림차순 - 증가하는 형태
'''
import sys
input = sys.stdin.readline


N,M = map(int,input().split())
graph = sorted(list(map(int,input().split())))
#chk = [False] * N
rs = []

def recur(start,depth):
    if depth == M:
        print(' '.join(map(str,rs)))
        return
    for i in range(start,N): #N만큼 돌긴하는데
        rs.append(graph[i])
        recur(i,depth+1)    
        rs.pop()
recur(0,0)
