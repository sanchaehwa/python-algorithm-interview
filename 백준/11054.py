import sys
class Solution:
    def lis2(self)->int:
        #수열의 크기
        N = int(sys.stdin.readline())
        #수열
        A = list(map(int,sys.stdin.readline().split()))
        #바이트닉 부분수열 : 오른쪽은 감소하는 형태여야하고 , 왼쪽은 증가하는 형태를 가지고 있어야한다. 
        #자기자신은 포함
        right_dp = [1] * N
        left_dp = [1] * N
        #왼쪽은 증가하는 형태
        for i in range(N):
            for j in range(i):
                if A[j] < A[i]:
                    right_dp[i] = max(right_dp[i],right_dp[j]+1)
        #오른쪽은 감소하는형태 거꾸로 새면 증가하는 형태
        for i in reversed(range(N)):
            for j in range(i+1,N):
                if A[i] > A[j]:
                    left_dp[i] = max(left_dp[i], left_dp[j]+1)
        #바이트닉 수열 
        result = 0
        for i in range(N):
            result = max(result, right_dp[i] + left_dp[i] -1)
        print(result)
solution = Solution()
solution.lis2()