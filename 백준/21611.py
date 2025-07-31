import sys
input = sys.stdin.readline

# 상, 하, 좌, 우 (문제 기준 1~4에 맞게 정의)
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# ← ↓ → ↑ (나선 순서)
spiral_dy = [0, 1, 0, -1]
spiral_dx = [-1, 0, 1, 0]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
magic = [list(map(int, input().split())) for _ in range(M)]
shark = (N//2, N//2)

bomb_count = [0, 0, 0, 0]

def get_spiral_order():
    order = []
    y, x = shark
    length = 1
    d = 0
    while True:
        for _ in range(2):
            for _ in range(length):
                y += spiral_dy[d]
                x += spiral_dx[d]
                if not (0 <= y < N and 0 <= x < N):
                    return order
                order.append((y, x))
            d = (d + 1) % 4
        length += 1

spiral_order = get_spiral_order()

def flatten_board():
    return [board[y][x] for y, x in spiral_order if board[y][x] != 0]

def update_board(spiral):
    for idx, (y, x) in enumerate(spiral_order):
        if idx < len(spiral):
            board[y][x] = spiral[idx]
        else:
            board[y][x] = 0

def cast_magic(d, s):
    d -= 1
    for dist in range(1, s+1):
        ny = shark[0] + dy[d] * dist
        nx = shark[1] + dx[d] * dist
        if 0 <= ny < N and 0 <= nx < N:
            board[ny][nx] = 0

def explode(spiral):
    global bomb_count
    new_spiral = []
    i = 0
    exploded = False
    while i < len(spiral):
        j = i
        while j < len(spiral) and spiral[i] == spiral[j]:
            j += 1
        if j - i >= 4:
            bomb_count[spiral[i]] += (j - i)
            exploded = True
        else:
            new_spiral.extend(spiral[i:j])
        i = j
    return new_spiral, exploded

def group_convert(spiral):
    new_spiral = []
    i = 0
    while i < len(spiral):
        j = i
        while j < len(spiral) and spiral[i] == spiral[j]:
            j += 1
        new_spiral.extend([j - i, spiral[i]])
        i = j
    return new_spiral[:N*N-1]

# 메인 로직
for d, s in magic:
    cast_magic(d, s)
    spiral = flatten_board()
    
    while True:
        spiral, exploded = explode(spiral)
        if not exploded:
            break
    
    spiral = group_convert(spiral)
    update_board(spiral)

# 결과 출력
print(bomb_count[1]*1 + bomb_count[2]*2 + bomb_count[3]*3)

# import sys
# input = sys.stdin.readline

# #N = 구슬의 개수 M은 마법을 한 경우의수
# N,M = map(int,input().split())
# graph = [list(map(int,input().split())) for _ in range(N)]
# magic = [list(map(int,input().split())) for _ in range(M)]
# shark_y,shark_x = N//2,N//2

# #방향을 바꾸는걸
# dy = [-1,1,0,0]
# dx = [0,0,1,-1]
# # cnt = 0 cnt_max = 1 c 
# #현재위치
# now = graph[shark_y][shark_x]
# bomb = 0
# wheel = []
# cnt = 0
# cnt_max = 1
# #상어 주변으로 마법을 시전을 했을때, 터진건 - 0
# for d,s in magic:
#     d -= 1 #d가 거리인데 여기서는 0부터시작했으니깐 문제는 1이고
#     for dist in range(1,s+1):
#         ny = shark_y + dy[d] * dist
#         nx = shark_x + dx[d] * dist
#         graph[ny][nx] = 0


# #언제 방향을 바꾸는가
# # [-1,0] : 1 , [1,0] : 2, [0,-1] : 3 , [0,1] : 4
# spiral_dy =[-1,0,1,0]
# sprial_dx = [0,1,0,-1]

# y,x = shark_y, shark_x #상어 위치부터 시작
# sprial_d = 0 #현재 방향 인덱스 
# cnt_max = 1 #처음은 1 
# cnt = 0  #방향 전환 횟수
# change = 0 #방향 전환 횟수 # 0 1 0 1 0 1 -?
# sprial = []
# while True:

#     y += spiral_dy[sprial_d]
#     x += sprial_dx[sprial_d]

#     if not (0 <= y < N and 0 <= x < N): #범위에서 벗어난 경우
#         break
#     sprial.append(graph[y][x])
#     cnt += 1
#     if cnt == cnt_max: # <- -> 이렇게 갔다고 하면 
#         cnt = 0 #cnt 초기화
#         sprial_d = (sprial_d+1) % 4  # 0과3 사이의 인덱스를 순회하기 위해
#         change += 1
#         if change == 2:
#             change = 0
#             cnt_max += 1
# #print(sprial)
# #여기서 4 연속되어있는걸 찾아야하는데 일단 0인 경우는 앞으로 밀자
# bomb = [0,0,0]
# spiral = [val for val in sprial if val != 0] #0이 아닌것부터
# if len(spiral) < N*N -1:
#     spiral += [0] * (N*N - 1 - len(spiral))
# #print(spiral)

# #이제 연속된거 찾아야하는데
# score = 0
# while True:
#     exploded = False
#     i = 0
#     new_spiral = []
#     while i < len(spiral): 
#         cnt = 1
#         while i + cnt < len(spiral) and spiral[i] == spiral[i+cnt]:
#             cnt += 1
#         if cnt >= 4:
#             score += spiral[i] * cnt
#             exploded = True
#         else: #연속이 아니라는건데
#             new_spiral += spiral[i:i+cnt]
#         i += cnt
#     spiral = new_spiral
#     if not exploded:
#         break
# print(score)


# #출력: 첫쨰 줄에 1 * 폭발한 1번 구슬의 개수 + 2 * 폭발한 2번 개수 + 3 * 3번 개수