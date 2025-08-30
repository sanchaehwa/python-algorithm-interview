import sys
input = sys.stdin.readline

#무방향이다 == 양방향이다
#정점의 개수 : N / 간선의 개수 : M

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]

#양방향 그래프

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)

def dfs(node):
    visited[node] = True
    for nxt in graph[node]:
        if not visited[nxt]:
            dfs(nxt)

components = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        components += 1
print(components)