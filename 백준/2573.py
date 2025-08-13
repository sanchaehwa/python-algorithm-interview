import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [-1,1,0,0]


#행 -- 열
N,M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]


def bfs_count(y,x,visited):
    q = deque()
    q.append((y,x))
    visited[y][x] = True
    while q:
        ny,nx = q.popleft()
        for i in range(4):
            ey = dy[i] + ny
            ex = dx[i] + nx
            if 0 <= ey < N and 0 <= ex < M:
                if not visited[ey][ex] and graph[ey][ex] != 0:
                    visited[ey][ex] = True
                    q.append((ey,ex))

def count_zero(y,x):
    cnt = 0
    for i in range(4):
        ex = dx[i]+x
        ey = dy[i]+y
        if 0 <= ey < N and 0 <= ex < M:
            if graph[ey][ex] == 0:
                cnt += 1
    return cnt

#초기 빙산 좌표 큐 생성 -- 빙산이 있는 경우에만 탐색한다
icebergs = deque()
for y in range(N):
    for x in range(M):
        if graph[y][x] != 0: #0이아닌 경우 -- 빙산인 경우
            icebergs.append((y,x))
year = 0
while icebergs:
    visited = [[False]*M for _ in range(N)]
    icebergCount = 0
    for (y,x) in icebergs:
        if not visited[y][x]:
            # 개수
            bfs_count(y,x,visited)
            icebergCount += 1
    if icebergCount >= 2: #2이상이면
        print(year)
        break

    # 1년 동안 녹을 양 계산 (graph 즉시 변경 금지)
    melt_list = []
    for (y, x) in icebergs:
        melt_list.append((y, x, count_zero(y, x)))

    # 녹인 후 살아남은 빙산 좌표 저장
    new_icebergs = deque()
    for (y, x, melt_amount) in melt_list:
        graph[y][x] = max(0, graph[y][x] - melt_amount)
        if graph[y][x] > 0:
            new_icebergs.append((y, x))
    icebergs = new_icebergs
    year +=1
    if not icebergs:
        print(0)
        break


    
# #빙산을 녹이는 과정
# def iceberg(y,x,temp):
#     cnt = 0
#     for i in range(4):
#         ex = dx[i] + x
#         ey = dy[i] + y
#         if 0 <= ey < N and 0 <= ex < M:
#             if graph[ey][ex] == 0: #상하좌우의 0의 개수만큼 graph[y][x] 줄어들고
#                 cnt += 1
#     temp[y][x] = max(0,graph[y][x] - cnt)

# def count(y,x):
#     visited[y][x] = True
#     for i in range(4):
#         ey = dy[i] + y
#         ex = dx[i] + x
#         if 0 <= ey < N and 0 <= ex < M:
#             if not visited[ey][ex] and graph[ey][ex] != 0:
#                 visited[ey][ex] = True
                # count(ey,ex)


# while True: #빙하의 개수가 2이상으로 분리가 될때까지 반복하는 구조
    
#     icebergCount= 0
#     visited = [[False]*M for _ in range(N)]

#     for y in range(N):
#         for x in range(M):
#             if not visited[y][x] and graph[y][x] != 0:
#                 count(y,x)
#                 icebergCount += 1
#     if icebergCount >= 2:
#         print(year)
#         break
#     if icebergCount == 0: #두덩어리로 분리되지 않은 경우
#         print(0)
#         break


#     temp = [[0]*M for _ in range(N)]
#     for y in range(N):    
#         for x in range(M):
#             if graph[y][x] != 0:
#                 iceberg(y,x,temp)
                

#     graph = temp #얼음이 녹은 graph로 갱신
#     year += 1

    