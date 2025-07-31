import sys
input = sys.stdin.readline

T = int(input()) # 3
for _ in range(T):
    N = int(input())
    num = list(map(int,input().split()))
    print(min(num),max(num))


