#수빈이가 있는 위치 N ---- 동생이 있는 위치 K 
#K까지 도달할때의 최소 방법

import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    N,K = map(int,input().split())
    visited = [False] * 100001
    graph = deque()
    graph.append([N,0])
    while graph:
        now,time = graph.popleft()
        if now == K:
            print(time)
            break
        #1초후에 갈수있는거리
        # case1 = now - 1
        # if not visited[case1]:
        #     visited[case1] = True
        #     graph.append([case1,time+1])
        # case2 = now + 1
        # if not visited[case2]:
        #     visited[case2] = True
        #     graph.append([case2,time+1])
        # case3 = 2 * now
        # if not visited[case3]:
        #     visited[case3] = True
        #     graph.append([case3,time+1])
        cmd = [now-1,now+1,2*now]
        for i in cmd:
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = True
                graph.append([i,time+1])
bfs()