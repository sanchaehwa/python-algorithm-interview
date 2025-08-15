dp = [0,1,2,4]
for i in range(4,14):  #11보다 작다 - 10 + 4
    dp.append(sum(dp[-3:])) #마지막 3개 요소
c = int(input())
for _ in range(c):
    N = int(input())
    print(dp[N])