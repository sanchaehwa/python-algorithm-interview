#브루트포스 => 모든 수를 다 대입해보면서 값을 찾아내는거, 가능한 조합
import sys
class Solution:
    def divisionSum(self)->int:
        #N = abc + (a+b+c)
        N = int(sys.stdin.readline())
        result = 0
        for i in range(1, N+1):
            #각 자리 분해
            nums = list(map(int,str(i)))
            result = sum(nums) + i
            #각자리의 합
            if result == N:
                print(i)
                break
            if i == N: #생성자가 없는 경우
                print(0)
solution = Solution()
solution.divisionSum()