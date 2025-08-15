import sys
input = sys.stdin.readline
#테스트 케이스 개수
T = int(input())
for _ in range(T):
    N = int(input())
    num = list(map(int,input().split()))
    visited = [False] * (N+1)
    cnt = 0
    for i in range(1,N+1):
        #첫번쨰 i를 visited 처리를 한다
        if not visited[i]:
            cnt += 1
            node = i # 1
            while not visited[node]:
                visited[node] = True
                node = num[node-1]

    print(cnt)
        