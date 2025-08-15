import sys
sys.setrecursionlimit(10**6)
cnt = 1
def dfs(node):
    global cnt
    #자기자신 count
    visited[node] = cnt
    cnt += 1    
    for i in graph[node]:
        if visited[i] == 0:
            dfs(i)

#정점의 수 : N / 간선의 수 : M
N,M,R = map(int,sys.stdin.readline().split())
graph = {i: [] for i in range(1,N+1)} #
for i in range(M):#M개 연결되어 있고
    A,B = map(int,sys.stdin.readline().split())
    graph[A].append(B)
    graph[B].append(A)
#정점은 오름차순으로 정렬되어있다 -> 작은거부터 방문한다는거
for i in graph:
    graph[i].sort()


visited = [0] * (N+1)
#시작정점 R을 시작정점으로 돌리면 시작 정점에서 방문할 수 없는 경우는 0으로 - visited를 0으로 초기화해줬으니깐
dfs(R)
# for i in range(R,N+1):
#     if visited[i] == 0:
#         dfs(i)
#         print(i)
    #시작 정점에서 방문할 수 없는경우
for i in range(1,N+1):
    print(visited[i])