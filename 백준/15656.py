import sys
input = sys.stdin.readline

#N개의 자연수 - M개를 고른 수열
N,M = map(int,input().split())
graph = sorted(list(map(int,input().split())))
chk = [False] * (N+1)
rs = []

def recur(num):
    if num == M:
        print(' '.join(map(str,rs)))
        return
    for i in range(1,N+1):
        if chk[i] == False:
            chk[i] = True
            rs.append(graph[i-1])
            recur(num+1)
            chk[i] = False 
            rs.pop()
recur(0)


