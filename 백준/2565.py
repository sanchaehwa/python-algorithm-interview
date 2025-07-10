import sys
class Solution:
    def electricWire(self)->int:
        N = int(sys.stdin.readline())
        A = []
        for _ in range(N):
            a,b = map(int,sys.stdin.readline().split())
            A.append([a,b])
        A.sort(key=lambda a:a[0]) #A 전봇대 기준 오름차순 정렬
        B = [] #B는 LIS eotkd
        result = [1] * N
        sum = 0
        for i in A:
            B.append(i[1])
        for i in range(N):
            for j in range(i):
                if B[j] < B[i]:
                    result[i] = max(result[i],result[j]+1)  #최대로 연결가능한 전깃줄 개수 리스트가 나오면
        sum = N - max(result)  #그중에서 최대를 전체에서 빼면 제거해야할 전깃줄 개수
        print(sum)
solution = Solution()
solution.electricWire()