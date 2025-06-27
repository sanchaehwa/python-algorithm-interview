import sys
from collections import deque

def bfs(words):
    A = words[0] #첫번째 문자열
    B = words[1] #두번째 문자열
    C = words[2] #세번째 = A 와 B를 순서는 섞이지않고 

    #A,B,C의 남은 글자수 : 탐색하고 나면 글자수가 줄겠지
    dq = deque([(len(A), len(B), len(C))])
    visited = [[False] * (len(B)+1) for _ in range(len(A)+1)]

    while dq:
        ai, bi, ci = dq.popleft() 
        if ai == bi == ci == 0: #A,B,C 모두 남은 글자수가없다 == A,B를 섞어서 문자를 만들었다
            return True
        if ci == 0:
            continue
        if ai > 0 and A[ai-1] == C[ci-1] and not visited[ai-1][bi]:
            visited[ai-1][bi] = True
            dq.append((ai-1, bi, ci-1))
        if bi > 0 and B[bi-1] == C[ci-1] and not visited[ai][bi-1]:
            visited[ai][bi-1] = True
            dq.append((ai, bi-1, ci-1))
    return False

N = int(sys.stdin.readline())
for i in range(N):
    words = sys.stdin.readline().strip().split()
    if bfs(words):
        print(f"Data set {i+1}: yes")
    else:
        print(f"Data set {i+1}: no")