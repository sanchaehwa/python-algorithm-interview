import sys
input = sys.stdin.readline

N,M = map(int,input().split())
#graph[r][c] => 현재위치 d => 현재 바라보는 위치 
r,c,d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
#청소하는 칸의 개수를 셀
cnt = 0
#북 - 남 - 서 - 동
dy = [-1,0,1,0]
dx = [0,1,0,-1]

#특정 조건 만족하는 경우, 한 계속 움직이고 - 1이다 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수없으면
while 1:
    if graph[r][c] == 0: #현재 위치가 청소가 안되어 있는 경우만
        #현재위치 청소
        graph[r][c] = 2 #청소한건  2로 표시
        cnt += 1
    sw = False #청소할곳이 있는지 
    #현재 방향을 기준으로 왼쪽 방향부터 
    for _ in range(4):
        d = (d + 3) % 4  # 왼쪽으로 회전
        ey = r + dy[d]
        ex = c + dx[d]
        if 0 <= ey < N and 0 <= ex < M and graph[ey][ex] == 0:
            r, c = ey, ex
            sw = True
            break
    #4빙향 모두 있지않은경우
    if sw == False:
        #뒤쪽 방향이 막혀있다 ==> 벽이 있다 후진할수없으면 작동 멈춤
        ny = r-dy[d]
        nx = c-dx[d]
        if 0 <= ny < N and 0 <= nx < M:
            if graph[ny][nx] == 1:
                break
            else:
                r,c = ny,nx
        else:
            break
print(cnt)