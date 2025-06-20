#R:베열에 있는 수의 순서를 뒤집고
#D:첫번쨰 수를 버리는 함수
#*배열이 비어있는데 D를 사용하면 에러 발생
import sys
from collections import deque
import ast
class Solution:
    def AC(self)->None:
        #테스트 케이스 수 
        t = int(sys.stdin.readline())
        for _ in range(t):
            #함수 입력
            f  = input()
            #리스트의 길이
            l = int(sys.stdin.readline())
            n = sys.stdin.readline().strip()
            if n == "[]":
                dq = deque()
            else: 
                num = ast.literal_eval(n)
                dq = deque(num)
            reverse = False
            error = False
            for i in f:
                if i == "R": #뒤집기
                    reverse = not reverse 
                # dq.reverse() #R 이 나올때마다 Reverse 하면 시간초과
                elif i == "D":
                    if not dq : #dq가 비어있는 경우에는 error
                        print("error")
                        error = True
                        break
                    else:
                        if reverse:
                            dq.pop() #오른쪽 끝 제거
                        else:
                            dq.popleft() #왼쪽 끝 제거
            if not error:
                if reverse:
                    dq.reverse() #이때 Reverse 한번에
                print("["+",".join(map(str, dq))+"]")
#[1,2,3,4] #[2,1]
solution = Solution()
solution.AC()