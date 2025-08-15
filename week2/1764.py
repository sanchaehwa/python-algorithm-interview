import sys
class Solution:
    def unheardOf(self)->None:
        N,M = map(int,sys.stdin.readline().split())
        unHeard = set(sys.stdin.readline().strip() for _ in range(N))
        unSee = set(sys.stdin.readline().strip() for _ in range(M))
        cnt = 0
        # for i in unHeard:
        #     for j in unSee:
        #         if i == j:
        #             result.append(i)
        #             cnt += 1
        result = unHeard & unSee
        cnt = len(result)
        print(cnt)
        for i in sorted(result):
            print(i)
solution = Solution()
solution.unheardOf()