import sys
input = sys.stdin.readline

N,M = map(int,input().split())
#결과값을 저장할 lst
rs = []
#방문 여부
visited = [False] * (N+1)

def recur(num):
    if num == M: #깊이까지 도달한거
        print(' '.join(map(str,rs)))
        return
    for i in range(1,N+1):
        if visited[i] == False:
            visited[i] = True
            rs.append(i)
            recur(num+1)
            visited[i] = False
            rs.pop()
            print(rs)
recur(0)