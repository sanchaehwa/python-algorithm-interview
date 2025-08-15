import sys
input = sys.stdin.readline

#N개의 자연수 - M개를 고른 수열
N,M = map(int,input().split())
graph = sorted(list(map(int,input().split())))
#chk = [False] * (N+1)
rs = []

def recur(num,start):
    if num == M:
        print(' '.join(map(str,rs)))
        return
    for i in range(start,N):
        #if chk[i] == False:
            #chk[i] = True
        if i > start and graph[i] == graph[i-1]:
            continue
        rs.append(graph[i])
        recur(num+1,i+1)
            #chk[i] = False 
        rs.pop()
recur(0,0)


