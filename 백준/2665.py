import sys
from collections import deque
input = sys.stdin.readline

def bfs(y, x):
    visited[y][x] = 0  # 시작점: 검은 방을 부순 횟수는 0
    q = deque()
    q.append((y, x))
    dy = [-1, 1, 0, 0]
    dx = [0, 0, 1, -1]
    
    while q:
        iy, ix = q.popleft()
        if iy == N - 1 and ix == N - 1:  # 끝까지 도달한 것
            print(visited[iy][ix])  # 최소로 부순 검은 방 개수 출력
            return
        for i in range(4):
            ey = dy[i] + iy
            ex = dx[i] + ix
            if 0 <= ey < N and 0 <= ex < N:
                # 흰 방일 경우 (비용 증가 없음)
                if graph[ey][ex] == 1:
                    # 아직 안 갔거나 더 적은 비용으로 갈 수 있다면
                    if visited[ey][ex] == -1 or visited[ey][ex] > visited[iy][ix]:
                       # print(visited[ey][ex])
                        visited[ey][ex] = visited[iy][ix]  # 비용 유지
                        q.appendleft((ey, ex))  # 우선 탐색
                # 검은 방일 경우 (비용 1 증가)
                elif graph[ey][ex] == 0:
                    if visited[ey][ex] == -1 or visited[ey][ex] > visited[iy][ix] + 1:
                        visited[ey][ex] = visited[iy][ix] + 1  # 비용 1 증가
                        q.append((ey, ex))  # 나중 탐색

N = int(input())
graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[-1] * N for _ in range(N)]  # -1: 아직 방문 안 한 상태
bfs(0, 0)