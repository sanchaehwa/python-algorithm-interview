import sys
input = sys.stdin.readline


A,P = input().split()
p = int(P)
k = []
num = []
while True:
    if A in num:
        print(num.index(A))
        break
    num.append(A)
    #A는 문자열이고 P도 문자열이라는것 
    k = [int(i)**p for i in A]
    A = str(sum(k))






