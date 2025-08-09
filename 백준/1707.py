import sys
input = sys.stdin.readline
#color = 0
def dfs(node):
    for i in graph[node]:
        if color[i] == -1: #방문하지않은경우에 이제 탐색
            color[i] = 1- color[node]
            dfs(i)
        
        elif color[i] == color[node]: #방문한경우를 방문한 경우 - 이분그래프
            global is_bipartite
            is_bipartite = False
        


#테스트 케이스
N = int(input())
#정점의 개수 V 간선의 개수 E
#E개의 줄을 거쳐서 
for _ in range(N):
    V,E = map(int,input().split())
    graph = {i : [] for i in range(1,V+1)}
    #visited = [False] * (V+1)
    color = [-1] * (V+1)  #방문하지않은건 -1 뱡문한건 1
    is_bipartite  = True
    for _ in range(E):
        A,B = map(int,input().split())
        graph[A].append(B)
        graph[B].append(A)
    for i in range(1,V+1):
        if color[i] == -1:
            color[i] = 0
            dfs(i)
    print("YES" if is_bipartite else "NO")