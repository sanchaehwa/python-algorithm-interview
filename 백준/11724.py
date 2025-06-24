import sys
sys.setrecursionlimit(10**6)

def dfs(node):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            dfs(i)
        
#정점의 개수 / 간선의 개수
N,M = map(int,sys.stdin.readline().split())
graph = {i: [] for i in range(1, N+1)}
for _ in range(M):
    u,v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [False] * (N+1)
cnt = 0
for i in range(1,N+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)
