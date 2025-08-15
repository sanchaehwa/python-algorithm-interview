import sys
input = sys.stdin.readline

#2진수 변환 내장 함수 사용하지않고 직접 구현
def binaryNum(num):
    result = []
    while num > 0:
        num,r = divmod(num,2)
        result.append(r)
    while len(result)<3: #3자리 이하이면 0으로 채운다
        result.append('0')
    return ''.join(map(str,reversed(result)))

#8진수 입력
N = input().strip()
if N == '0':
    print(0)
#N이면 앞에는 0
else:
    ls = [] #이진수 담을거
    ls.append(str(int(binaryNum(int(N[0])))))
    for i in N[1:]:
        ls.append(binaryNum(int(i)))
    print(''.join(ls))