import sys

class Solution:
    def cmd(self)->str:
        #몇개 입력
        N = int(sys.stdin.readline())
        file = [sys.stdin.readline().strip() for _ in range(N)]
        #자리수별로 비교
        file1 = list(file[0])

        for i in range(1,N):
            for j in range(len(file1)):
                if j >= len(file[i]) or file1[j] != file[i][j]:
                    file1[j] = '?'
        print(''.join(file1))
solution = Solution()
solution.cmd()