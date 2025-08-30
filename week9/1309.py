import sys 
input = sys.stdin.readline



N = int(input())
dp = [[0] * 3 for _ in range(N+1)]


# 0 - 아무것도 선택하지 않거나  / 1 - 위에만 선택했을때 아래 - 아무것도 선택 / 2 - 아래만 선택 위 - 아무것도 선택
dp[1][0] = 1
dp[1][1] = 1
dp[1][2] = 1


for i in range(2,N+1):
    for j in range(3):
        if j == 0:
            dp[i][j] =(dp[i-1][j] + dp[i-1][j+1] + dp[i-1][j+2]) % 9901
        elif j == 1:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % 9901
        else:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j-2]) % 9901
print(sum(dp[N])%9901)