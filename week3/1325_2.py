from collections import deque
def bfs(start):
    queue = deque([start])
    visited = [0] * (N+1)
    visited[start] =1
    cnt = 1
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
            cnt +=1
    return cnt



#컴퓨터수 
# N = int(input())
# #연결된 수 
# M = int(input())
N,M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    K,J = map(int,input().split())
    graph[J].append(K)    
connections = [0] * (N+1)
for i in range(N):
    connections[i] = bfs(i)
max_count = max(connections)
answer = [i for i in range(1,N+1) if connections[i] == max_count]
print(' '.join(map(str,answer)))