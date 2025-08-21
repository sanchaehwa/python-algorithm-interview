import sys
input = sys.stdin.readline

T = int(input())
# 언제나 2행 2열이다
for _ in range(T):
    N = int(input())
    dp = [[0] * N for _ in range(2)]
    sticker = [list(map(int,input().split())) for _ in range(2)]

    #스티커 길이가 1인 경우
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]

    if N == 1:
        print(max(dp[0][0],dp[1][0]))
        continue

    #스티커 길이가 2인경우
    dp[0][1] = sticker[0][1] + sticker[1][0]
    dp[1][1] = sticker[0][0] + sticker[1][1]
    
    if N == 2:
        print(max(dp[0][1],dp[1][1]))
        continue
    
    #스티커 길이가 2이상인경우
    for i in range(2,N):
        dp[0][i] =  max(dp[1][i-2],dp[1][i-1]) + sticker[0][i]
        dp[1][i] =  max(dp[0][i-2],dp[0][i-1]) + sticker[1][i]
    print(max(dp[0][-1],dp[1][-1]))


