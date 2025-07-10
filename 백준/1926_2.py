import sys
input = sys.stdin.readline
'''
1. 아이디어 
    - 2중 For 문 1이 나올때마다 && 방문하지않은것
    - 그림 개수 + 1 / 최대값을 갱신
    - 시간복잡도 O(v + v4) = O(5v) = *M,N의 최대가 500이니깐 5 * 500 * 500 = 250000 * 5 
    - E = 4 * (m*n)
'''
def bfs(y,x): #y = i, x = j
    rs = 1 
    visited[y][x] = 1
    q = [(y,x)]
    #상하좌우
    x = [0,0,1,-1]
    y = [-1,1,0,0]

    #queue에 더이상 들어가지않을떄 
    while q:
        ey , ex = q.pop()
        for k in range(4):
            dy = ey + y[k]
            dx = ex + x[k]
            if 0 <= dy < M and 0 <= dx < N:
                if visited[dy][dx] == 0 and graph[dy][dx]:
                    rs += 1
                    visited[dy][dx] = 1
                    q.append((dy,dx))
    return rs
# M,N 입력
M,N = map(int,input().split())
#M * N 만큼 입력
graph = [list(map(int,input().split())) for _ in range(M)]
#방문 기록
visited = [[0] * N for _ in range(M)]
#2중 For문 1이 나올때마다 방문하지않은것에대한 bfs 수행
# 전체 그림 갯수
cnt = 0
# 그림 크기
maxV = 0

for i in range(M): #y
    for j in range(N): #x
        if graph[i][j] == 1 and visited[i][j] == 0:
            # 전체 그림 갯수를 + 1
            # BFS > 그림 크기 구하고 -> 최대값 갱신
            cnt += 1 
            maxV = max(maxV, bfs(i,j))
print(cnt)
print(maxV)