# import sys
# from itertools import permutations
# class Solution:
#     def thirty(self)->int:
#         N = list(map(int,sys.stdin.readline().strip()))
#         l = len(N) 
#         result = set() #중복 제거
#         for i in permutations(N,l): #N! 시간복잡도 증가로 시간초과
#             k = int(''.join(map(str, i)))            
#             if k % 30 == 0:
#                 result.add(k)
#         if result:
#             print(max(result))
#         else:
#             print(-1)
# solution = Solution()
# solution.thirty()
import sys
class Solution:
    def thirty(self)->int:
        N = list(map(int,sys.stdin.readline().strip()))
        #0이 포함되어있는지 확인 - 10의 배수
        if 0 not in N:
            print(-1)
            return
        #3의 배수
        if sum(N) % 3 != 0:
            print(-1)
            return
        N.sort(reverse=True)
        print(''.join(map(str,N)))
solution = Solution()
solution.thirty()