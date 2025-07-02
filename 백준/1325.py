# import sys
# sys.setrecursionlimit(10**6)

# def dfs(node):
#     visited[node] = True
#     cnt = 1 #자기 자신을 포함
#     for n in graph.get(node,[]):  # 3--1 , 3---2'
#         if not visited[n]:
#             cnt += dfs(n)
#     return cnt

# N,M = map(int,sys.stdin.readline().split()) #N은 컴퓨터수 , M은 관계수
# graph = dict()
# result = {}

# for _ in range(M):
#     #c1이 Key, r1이 Value
#     c1,r1 = map(int,sys.stdin.readline().split())
#     if r1 not in graph:
#         graph[r1] = []
#     graph[r1].append(c1)

# for node in range(1,N+1):
#     visited = [False] * (N+1)
#     if not visited[node]:
#         result[node] = dfs(node) -1
# #결과 출력
# r = [k for k,v in result.items() if max(result.values())==v] 
# print(' '.join(map(str,r)))

# 시간 초과로 bfs (한번에 (최단) = bfs 접근?)
from collections import deque
def bfs(start):
    queue = deque([start])
    visited = [0] * (N+1)
    visited[start] = 1 #자기 자신은 방문 표시
    count = 1 #자기 자신

    while queue:
        v = queue.popleft()

        # print(v)
        for i in graph[v]:
            #print(i)
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
            count += 1

    return count
#N : 컴퓨터 수, M: 관계수
N,M = map(int,input().split())
#연결 정보 저장 리스트
graph = [[] for _ in range(N+1)]
for _ in range(M):
    #A가 신뢰하면 B도 가능함 - 단뱡향 
    A,B = map(int,input().split())
    graph[B].append(A)
#print(graph)
#컴퓨터 별로 연결된
connections = [0] * (N+1)

for i in range(1, N+1):
    connections[i] = bfs(i)

print(connections)

max_count = max(connections)
answer = [i for i in range(1, N+1) if connections[i] == max_count]
print(' '.join(map(str,answer)))
