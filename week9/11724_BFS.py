import sys
from collections import deque

input = sys.stdin.readline

#M - y , N - x
N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    A,B = map(int,input().split())
    graph[A].append(B)
    graph[B].append(A)
visited = [False] * (N+1)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        node = q.popleft()
        for nxt in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

components = 0
for i in range(1,N+1):
    if not visited[i]:
        bfs(i)
        components += 1
print(components)