import sys
from collections import deque
def bfs(A,B):
    a = list(A)
    b = list(B)
    #연산홧수
    result = [[0] * len(b) for _ in range (len(a))]
    dq = deque[(len(a),len(b))]
    target =[]
    while dq:
        ai,bi = deque.popleft()
        if a[ai-1] != b[bi-1] and result[bi][ai] == 0:
            target.append(b[bi-1])
            result[bi][ai] = 1
            if target == a[ai-1:]:
                



A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()
bfs(A,B)

