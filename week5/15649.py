'''
백트래킹은 순열, 조합, 부분집합 등에서 '길이 M'인 결과를 만들 때 사용한다.
재귀함수는 depth (현재까지 고른 원소의 개수)를 기준으로 종료 조건을 판단한다.

- 중복 없이 N개 중 M개 고르려면 visited[] 배열로 방문 여부를 관리한다.
- 선택한 값은 rs[] 같은 배열에 저장한다.

시간 복잡도는 문제 유형에 따라 다르다:
- 중복 허용 순열: N^M
- 중복 없이 순열: P(N, M) = N! / (N - M)!
- 중복 없이 조합: C(N, M) = N! / (M!(N - M)!)
- N이 작을 때 (보통 8~10 이하), 백트래킹으로 완전탐색이 가능하다.
'''  

import sys
input = sys.stdin.readline

N,M = map(int,input().split()) #깊이는 M
#선택한 값을 입력 배열
rs = []
chk = [False] * (N+1) #1부터라서 앞에 0번째는 제외하고 나머지

def recur(num):
    if num == M:
        print(' '.join(map(str, rs)))
        return 
    for i in range(1,N+1): #N만큼 
        if chk[i] == False:
            chk[i] = True #방문처리
            rs.append(i)
            recur(num+1)
            chk[i] = False
            rs.pop()
recur(0)