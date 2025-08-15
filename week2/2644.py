import sys
sys.setrecursionlimit(10**6)
#촌수 계산 : x ---y까지의 간선의 수
def dfs(node,depth):
    global result
    visited[node] = True
    if node == y:
        result = depth
        return
    for i in graph[node]:
        if not visited[i]:
            dfs(i,depth+1)



# 전체 사람의 수 
n = int(sys.stdin.readline())
#촌수를 계산해야하는 서로 다른 두사람의 번호
x,y = map(int,sys.stdin.readline().split())
#부모 자식들간의 관계의 개수 m : 간선의 개수
r = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(r):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n+1)
result = -1 
#x부터 탐색해서 y가 나오는 
dfs(x,0)
print(result)