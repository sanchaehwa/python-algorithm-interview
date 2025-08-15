import sys
input = sys.stdin.readline




N = int(input())
#교실
graph = [[0] * N for _ in range(N)]
students = {}
order = []
#앞에는 학생번호 ---- 뒤에는 좋아하는 사람
for _ in range(N*N):
    data = list(map(int,input().split()))
    student = data[0]
    favorites = data[1:]
    students[student] = favorites
    order.append(student)
#상하좌우 탐색
dy = [-1,1,0,0]
dx = [0,0,1,-1]
for s in order:
    favoritesStudent  = students[s]
    candidates = [] #후보지
    for y in range(N):
        for x in range(N):
            if graph[y][x] != 0:
                continue
            like_cnt = 0
            empty_cnt = 0
            for i in range(4):
                ex = dx[i] + x
                ey = dy[i] + y
                if 0 <= ex < N and 0 <= ey < N:
                    if graph[ey][ex] == 0:
                        empty_cnt += 1
                    elif graph[ey][ex] in favoritesStudent:
                        like_cnt += 1
            candidates.append((-like_cnt,-empty_cnt,y,x)) #정렬을 위한 음수 처리
    candidates.sort()
    _,_,seat_y,seat_x = candidates[0]
    graph[seat_y][seat_x] = s

# 앉히고 탐색해 주변에 좋아하는 사람이 얼마있는지 그리고 더해서 값 도출
#print(graph)
cnt = 0
score_table = [0,1,10,100,1000]
for i in range(N):
    for j in range(N):
        target = graph[i][j] 
        favoritesStudent  = students[target]
        like_cnt = 0
        for d in range(4):
            ey = dy[d] + i
            ex = dx[d] + j
            if 0 <= ex < N and 0 <= ey < N:
                if graph[ey][ex] in favoritesStudent:
                    like_cnt += 1
        cnt += score_table[like_cnt]
print(cnt)
        
