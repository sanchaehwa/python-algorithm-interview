import sys

def bfs(A,B):
    a = list(A)
    b = list(B)
    #연산홧수
    result = [[0] * len(b) for _ in range (len(a))]
    print(result)


A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()
bfs(A,B)

