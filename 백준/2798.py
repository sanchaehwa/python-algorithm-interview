import sys
class Solution:
    def blackJack(self)->int:
        N,M = map(int,sys.stdin.readline().split())
        card = list(map(int,sys.stdin.readline().split()))
        result = []
        sum = 0
        for i in range(N):
            for j in range(i+1,N):
                for k in range(j+1,N):
                    sum = card[i] + card[j] + card[k]
                    if sum <= M:
                        result.append(sum)

        print(max(result))
solution = Solution()
solution.blackJack()