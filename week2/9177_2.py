# queue 가 0으로 채워져있다 하면 3번쨰 단어를 만들수있는거
# 한번 체크한곳은 두번 체크안하게 Visited 로 처리
import sys
from collections import deque
def bfs(words):
    A,B,C  = words[0],words[1],words[2]
    dq = deque([(len(A),len(B),len(C))])
    visited = [[False] * (len(B) + 1) for _ in range((len(A)+1)) ]

    while dq:
        ai, bi, ci = dq.popleft() 
        if ai == bi == ci==0:
            return True
        if ci == 0:
            continue
        if ai > 0 and A[ai-1] == C[ci-1] and not visited[ai-1][bi]:
            visited[ai-1][bi] = True
            dq.append((ai-1,bi,ci-1))

        
        if bi > 0 and B[bi-1] == C[ci-1] and not visited[ai][bi-1]:
            visited[ai][bi-1] = True
            dq.append((ai,bi-1,ci-1))
    return False
N = int(sys.stdin.readline())
for i in range(N):
    words = sys.stdin.readline().strip().split()
    if bfs(words):
        print(f"Data set {i+1}: yes")
    else:
        print(f"Data set {i+1}: no")
