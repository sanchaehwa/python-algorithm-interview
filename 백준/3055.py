import sys
from collections import deque
input = sys.stdin.readline
R,C = map(int,input().split()) #R : y, C: x
graph = [list(input().strip()) for _ in range(R) ]
q1 = deque() #물의 위치
q2 = deque() #고슴도치의 위치
visited = [[0] * C for _ in range(R)]
#비버의 위치를 찾고 Q1에 넣고, 고슴도치의 위치를 찾고 Q2에 넣어
for i in range(R):
    for j in range(C):
        if graph[i][j] == 'S': #고슴도치의 위치
            q2.append((i,j))
            visited[i][j] = 1 #방문 처리
        if graph[i][j] == '*': #물의 위치
            q1.append((i,j))
def bfs():
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]
    time = 0
    #물과 고슴도치는 동시에 움직여야함
    while q2:
        #물의 이동
        for _ in range(len(q1)):
            y,x = q1.popleft()
            for i in range(4):
                wy = y + dy[i]
                wx = x + dx[i]
                if 0 <= wy < R and 0 <= wx < C:
                    if graph[wy][wx] == '.':
                        graph[wy][wx] = '*'
                        q1.append((wy,wx))
            #고슴도치의 이동
        for _ in range(len(q2)):
            ey,ex = q2.popleft()
            for i in range(4):
                ny = dy[i] + ey
                nx = dx[i] + ex
                if 0 <= ny < R and 0 <= nx < C:
                    if graph[ny][nx] == 'D':
                        print(time + 1)
                        exit()

                    if graph[ny][nx] == '.' and visited[ny][nx] == 0:
                        visited[ny][nx] = 1                        
                        q2.append((ny,nx))
                   
        time += 1
                    
#다 못돌아간 경우
    print("KAKTUS")
bfs()




#가장 빠른 시간 == bfs
#물이 찰 예정인 칸으로 고슴도치는 이동할 수 없다 == 그럼 고슴도치가 빨리 도착해야하는
#고슴도치는 상하좌우로 이동 -- 물, 고슴도치 물을 통과 * 