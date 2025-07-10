import sys
sys.setrecursionlimit(10**6)

def dfs(i,j):
    visited[i][j] = 1 #방문처리
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    w,s = 0,0
    if graph[i][j] == 'o': #탐색 위치가 양이거나 늑대인경우에 +1
        s += 1
    if graph[i][j] == 'v':
        w += 1
    for k in range(4):
        x = j + dx[k]
        y = i + dy[k]
        if 0 <= x < C and 0 <= y < R:
            if graph[y][x] != '#' and not visited[y][x]: #탐색하면서 양과,늑대를 발견했을때 늑대와 양의 수를 증가
                nw,ns=dfs(y,x)
                w += nw
                s += ns
    return w,s
        
R,C = map(int,sys.stdin.readline().split())
graph =[list(sys.stdin.readline().strip()) for _ in range(R)]
# for i in range(R):
#     for j in range(C):
#         if graph[i][j] == '.': #필드
#             graph[i][j] = '0'
#         elif graph[i][j] == '#': #울타리
#             graph[i][j] = '1'
visited = [[0] * C for _ in range(R)]
total_wolf = 0
total_sheep = 0
result = []
for i in range(R):
    for j in range(C):
        if graph[i][j] != '#' and not visited[i][j]:#울타리가 아닌 필드랑 양, 늑대가있는경우만 탐색
            w, s = dfs(i,j)
            if s > w: #양이 더크면 
                total_sheep += s
            else: #늑대가더 크면
                total_wolf += w

result.append(total_sheep)
result.append(total_wolf)
print(' '.join(map(str,result)))
        
