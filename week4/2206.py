import sys
from collections import deque

input = sys.stdin.readline
'''
아이디어
1. (1,1) 출발 지점에서 (1)인 지점까지 이동하고 그 (1,1) 지점에서 다시 (6,4) (M,N) 지점까지 이동하면 그걸 더하고 최소값으로 갱신해나가면 되지않는강>
2. 1번 아이디어 - K => 벽을 뚫은 횟수 : 1번 초과하면 안되는걸로 하면 된다 
'''
N,M = map(int,input().split()) #N : y, M : x
graph = [list(map(int,input().strip())) for _ in range(N)]

visited = [[[0] * 2  for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1 #시작지점은 1 방문처리
q = deque()
q.append((0,0,0))
def bfs():
    while q:
        dx = [0,0,1,-1]
        dy = [-1,1,0,0]
        ey,ex,k = q.popleft()
        if ey == N-1 and ex == M-1:
            print(visited[ey][ex][k]) #BFS 자체가 최단거리를 보장해주고 있음  /시작지점 끝나는지점 모두포함이니깐 근데 시작지점에 이미 1로 방문처리했으니깐 
            exit()
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] == 0 and visited[ny][nx][k] == 0:
                    visited[ny][nx][k] = visited[ey][ex][k]+1
                    q.append((ny,nx,k))
                elif k == 0 and graph[ny][nx] == 1 and visited[ny][nx][1] == 0:
                    visited[ny][nx][1] = visited[ey][ex][k]+1
                    q.append((ny,nx,1))
                
bfs()
#불가능할떄는 -1 출력
print(-1)
                    
                    
                    

