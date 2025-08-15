import sys
sys.setrecursionlimit(100000)

dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    #조건 1
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    #조건 2
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    
    if dp[a][b][c] != 0:
        return dp[a][b][c]
    #조건3
    if a < b and b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    #조건4
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")