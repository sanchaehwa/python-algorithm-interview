import sys
input = sys.stdin.readline
result = 0.0
def dfs(y,x,percent,moved):
    global result
    visited[y][x] = True #처음 방문한 곳
    dy = [-1,1,0,0]
    dx = [0,0,1,-1]
    if moved == N:
        result += percent
        return
    for i in range(4):
    
        ey = dy[i] + y
        ex = dx[i] + x
        #동서 남북에 따라이제 이동 확률을 서로 곱하고
        if 0 <= ey < 2*N+1 and 0 <= ex < 2*N+1:
            if not visited[ey][ex]:
                visited[ey][ex] = True #방문처리
                dfs(ey,ex,percent*per[i],moved+1)
                #방문하지 않은곳에서 -- 방문하고 -- 다시 방문할수있다는게 EENE
                visited[ey][ex] = False
    


N,E,W,NO,S = map(int,input().split())
visited = [[False] * (2*N+1) for _ in range(2*N+1)]
#E W NO S
per = [E,W,NO,S]
per = [p/100 for p in per]
#확률을 담을 부분
#이동 횟수
#로봇이 처음 위치한곳 - 
start = N 
visited[start][start] = True
dfs(start,start,1.0,0)
print(result)