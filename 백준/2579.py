#첫번째 계단 개수
N = int(input())
#두번째 계단 
S = [int(input()) for _ in range(N)]
#DP
dp = [0] * N

#첫번째, 두번째 계단 밖에 없는 경우
if len(S) <= 2:
    print(sum(S))
else: #계단이 3개 이상인경우
    #첫번째 계단
    dp[0] = S[0]
    #두번쨰 계단 * 첫번째 계단 올라가고 두번쨰 계단
    dp[1] = S[0] + S[1]
    #두칸 식 , 한칸식
    for i in range(2,N):
        dp[i] = max((dp[i-3] + S[i] + S[i-1]) , (dp[i-2] + S[i]))
    print(dp[-1])
 