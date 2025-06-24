import sys
sys.setrecursionlimit(10**6)

def dfs(node,parent):
    visited[node] = True
    parents[node] = parent
    for i in graph[node]:
        if not visited[i]:
            dfs(i,node)
#개수
N = int(sys.stdin.readline())
#graph = {i: [] for i in range(1, N+1)}
graph = [[0] for _ in range(N+1)]
for _ in range(N-1): #간선의수는 노드의 -1
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [False] * (N+1) #1번부터 시작
parents = [0] * (N+1) #1번 노드 부터 시작
dfs(1,0)
for i in parents[2:]:
    print(i)