import sys
input = sys.stdin.readline

N = int(input())
#3kg, 5kg
#개수
#5kg로 나눠떨어지는경우
if N % 5 == 0:
    print(N // 5)
#5로 나눠떨어지지않는 경우
else:
    p = 0
    while N > 0:
        N -= 3
        p += 1
        if N % 5 == 0:
            p += N // 5
            print(p)
            break
        elif N == 1 or N == 2:
            print(-1)
            break
        elif N == 0:
            print(p)
            break