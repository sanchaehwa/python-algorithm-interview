import sys
from collections import deque
input = sys.stdin.readline


#bfs 
def bfs(s):
    lst2 = []
    q = deque()
    q.append(s)
    visited1[s] = 1
    while q:
        start = q.popleft()
        lst2.append(start)
        for i in sorted(graph[start]):
            if not visited1[i]:
                q.append(i)
                visited1[i] = 1
    return lst2


def dfs(s,lst1):
    visited2[s] = 1
    lst1.append(s)
    for i in sorted(graph[s]):
        if not visited2[i]:
            dfs(i,lst1)



#정점의 개수: N, 간선의 개수: M, 탐색을 시작할 정점의 번호: V
N,M,V = map(int,input().split())
graph = {i: [] for i in range(1,N+1)}
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited1 = [0] * (N+1)
visited2 = [0] * (N+1)
result2 = bfs(V)

result1 = []
dfs(V,result1)
print(' '.join(map(str,result1)))
print(' '.join(map(str,result2)))
