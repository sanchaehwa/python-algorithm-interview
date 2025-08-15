import sys
input = sys.stdin.readline

#연도
N = int(input())
#4의 배수이면서 100의 배수가 아닐떄 또는 400의 배수 
if (N % 4 == 0 and N % 100 != 0) or (N % 400 == 0):
    print(1)
else:
    print(0)