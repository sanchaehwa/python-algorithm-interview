import sys
def dfs(x,y):
    visited[x][y]=True
    cnt = 0
    x1 = [0,0,1,-1]
    y1 = [-1,1,0,0]
    for i in range(4):
        dx = x1[i] + x 
        dy = y1[i] + y
        if 0 <= dx < N and 0 <= dy <N:
            if rain[dx][dy] == 0 and not visited[dx][dy]:
                dfs(dx,dy)



#행 과 영의 개수를 나타내는 N

N = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
max_rain = max(map(max,graph))
#안전영역 list
safe = []
current = 0 #현재 위치
#비에 잠긴 영역을 표시된 graph
for h in range(max_rain+1):
    #비의 양 보다 이하인것은 물에 잠기는 영역 - 1
    rain = [[0]*N for _ in range(N)] #0으로 초기화
    visited = [[False] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if graph[x][y] <= h:
                rain[x][y] = 1
    total = 0
    for i in range(N):
        for j in range(N):
            if rain[i][j] == 0 and visited[i][j] == False:
                dfs(i,j)
                total += 1
    
    safe.append(total)
print(max(safe))