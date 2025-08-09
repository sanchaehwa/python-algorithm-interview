import sys
input = sys.stdin.readline

#M개를 고른 경우
N,M = map(int,input().split())
graph = sorted(list(map(int,input().split())))
chk = [False] *N
rs = []
def recur(num):
    if num == M:
        print(' '.join(map(str,rs)))
        return
    used_level_this = set()
    for i in range(N):
        if chk[i] == False:
            if graph[i] not in used_level_this:
                chk[i] = True #사용하고 set에 넣고 
                used_level_this.add(graph[i])
                rs.append(graph[i])
                recur(num+1)
                chk[i] = False
                rs.pop()
recur(0)
        