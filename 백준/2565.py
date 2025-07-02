import sys
class Solution:
    def electricWire(self)->int:
        N = int(sys.stdin.readline())
        A = []
        for _ in range(N):
            a,b = map(int,sys.stdin.readline().split())
            A.append([a,b])
        A.sort(key=lambda a:a[0])
        B = []
        result = [1] * N
        sum = 0
        for i in A:
            B.append(i[1])
        for i in range(N):
            for j in range(i):
                if B[j] < B[i]:
                    result[i] = max(result[i],result[j]+1)
        sum = N - max(result)
        print(sum)
solution = Solution()
solution.electricWire()