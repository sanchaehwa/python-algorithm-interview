import sys
input = sys.stdin.readline

# M,N M 이 깊이 N이 몇개의 숫자를 받을지
M , N = map(int,input().split())
alp = list(input().split())
alp.sort() #사전 순으로 정렬
#최소 한개의 모음이 있는지 확인을 하기위한 모음 
lst = ['a','e','i','o','u']
rs = []
def recur(start,depth):
    if depth == M:
        mo = sum(1 for x in rs if x in lst)
        ja = M - mo
        if mo >= 1 and ja >= 2:
            print(''.join(rs))
        return
    for i in range(start,N):
        rs.append(alp[i])
        recur(i+1,depth+1)
        rs.pop()
recur(0,0) # 맨 처음 요소 부터 탐색해야하니깐