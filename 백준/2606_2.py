
#컴퓨터수 입력
n = int(input()) 
#간선 수 입력
c = int(input())
#양방향 연결
graph = [[] for _ in range(n+1)]
for _ in range(c):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#방문 여부 * False로 초기화 
visited = [False] * (n+1)
#감염된 컴퓨터의 수 
cnt = 0
def dfs(node):
    global cnt
    visited[node] = True
    for i in graph[node]: #현재 노드랑 연결되어있는 이웃 노드 순회
        #방문하지않는 노드인 경우
        if not visited[i]:
            cnt += 1
            #재귀호출 연결된 컴퓨터를 
            dfs(i)
dfs(1)
print(cnt)
