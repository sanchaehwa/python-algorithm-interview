import sys
from collections import deque
input = sys.stdin.readline

#dfs 수행
def dfs(n): 
    visited[n] = 1 #방문처리
    lst1.append(n)
    for i in sorted(graph[n]):
        if visited[i] == 0:
                dfs(i)
#bfs 수행
def bfs(k):
    q = deque()
    q.append(k)
    visited1[k] = 1

    while q:
        j = q.popleft()
        lst2.append(j)
        for i in sorted(graph[j]):
            if visited1[i] == 0:
                q.append(i)
                visited1[i] = 1 



# 정점이 개수 N , 간선의 개수 M , 시작 정점의 번호 V 
N,M,V = map(int,input().split())
graph = {i: [] for i in range(1, N+1)}
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (N+1)
lst1 = []
visited1 = [0] * (N+1)
lst2 = []
dfs(V)
bfs(V)
print(' '.join(map(str,lst1)))
print(' '.join(map(str,lst2)))


