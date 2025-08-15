import sys
input = sys.stdin.readline

#N개의 자연수 - M개를 고른 수열
N,M = map(int,input().split())
graph = sorted(list(map(int,input().split())))
#chk = [False] * (N)
rs = []

def recur(depth):
    if depth == M:
        print(' '.join(map(str,rs)))
        return
    for i in range(N):
        #if chk[i] == False:
            #chk[i] = True
        rs.append(graph[i])
        recur(depth+1)
            #chk[i] = False 
        rs.pop()
recur(0)


