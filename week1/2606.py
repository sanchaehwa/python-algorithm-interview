import sys
sys.setrecursionlimit(10**6)

#현재 탐색하고 있는 컴퓨터
def dfs(node):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]: #아직 방문하지않는 컴퓨터면 재귀호출
            dfs(i) 
#컴퓨터수 입력
computer = int(input())
#연결되어있는 컴퓨터쌍
connected = int(input())
graph = {i: [] for i in range(1, computer+1)}
for _ in range(connected):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (computer+1) #1부터 7 까지 

# 이후 DFS(1) 호출
cnt = 0 #바이러스에 감염된 수
dfs(1) # 1번 컴퓨터부터
for i in range(2,computer+1): #1 제외하고
    if visited[i]:
        cnt += 1
        
print(cnt)