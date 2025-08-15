import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(y,x):
    
    if graph[y][x] == 'H':
        return 0 #이동불가
    
    if visited[y][x]:
        print(-1)
        sys.exit(0)

    if dp[y][x] != -1: 
        return dp[y][x]
   
    visited[y][x] = True
    dp[y][x] = 1
    current = int(graph[y][x])
    

    dy = [-1,1,0,0]
    dx = [0,0,1,-1]
    
    for i in range(4):
        ny = dy[i] * current + y
        nx = dx[i] * current + x
        if 0 <= ny < N and 0 <= nx < M:
            dp[y][x] = max(dp[y][x],dfs(ny,nx)+1)
    visited[y][x] = False
    return dp[y][x]



#세로 - N,가로 - M
N,M = map(int,input().split())
graph = [list(input().strip()) for _ in range(N)]
dp = [[-1] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
#최대 
answer = 0
answer = dfs(0,0) #출발점인 경우가 대다수라고 생각하기
print(answer)