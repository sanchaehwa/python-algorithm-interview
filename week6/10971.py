import sys
input = sys.stdin.readline


def dfs(y,x):
    visited[y][x] = True
    lst =[y,x]
    for i in range(x,N):
        lst.append(i)
    print(lst)



N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

for i in range(4):
    for j in range(1,4):
        if graph[i][j] != 0 and not visited[i][j]:
            dfs(i,j) #출발점
           
            
