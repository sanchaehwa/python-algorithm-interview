def dfs(x,y):
    #방문 처리
    visited[x][y] = True 
    #상(-1,0),하(1,0),좌(0,-1),우(0,1)
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx , ny = dx+x , dy+y
        if 0 <= nx < r and 0 <= ny < c:
            if field[nx][ny] == 1 and not visited[nx][ny]: #방문하지않는 노드
                dfs(nx,ny)
#테스트 케이스 개수 입력
n = int(input())
#n번 - c만큼 입력받는다 
for _ in range(n):
    # 가로길이, 세로길이, 배추 개수
    c,r,k = map(int,input().split())
    #배추 밭 
    field = [[0] * c for _ in range(r)]
    #방문
    visited = [[False] * c for _ in range(r)]
    for _ in range(k):
        c_1,c_2 = map(int,input().split())
        field[c_2][c_1] = 1
    cnt = 0
    for i in range(r):
        for j in range(c):
            if field[i][j] == 1 and not visited[i][j]:
                dfs(i,j)
                cnt += 1
    print(cnt)
