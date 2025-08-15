import sys
from collections import deque

input = sys.stdin.readline
#테스트 케이스 개수
T = int(input()) 
def bfs():
    for _ in range(T):
        #입력수 --- 만들어야 할 수 
        A,B = map(int,input().split())
        #방문 배열
        visited = [False] * 10000 #최대가 10000이니깐
        #계산 결과를 담을 레지스트리
        reg = deque()
        reg.append([A,''])
        while reg:
            n,c = reg.popleft() #n : 숫자, c : 명령어
            if n == B: #만들어야할 수와 같으면 출력
                print(c)
                break
            #D의 경우를 실행할때 
            D = (n * 2) % 10000
            if not visited[D]: #D라는 숫자를 접근하지않았다면
                visited[D] = True
                reg.append([D,c+'D'])
            #S의 경우를 실행을 할때
            S = (n - 1) % 10000 #0이면 9999
            if not visited[S]:
                visited[S] = True
                reg.append([S,c+'S'])
            #L의 경우 실행
            L =  (n % 1000) * 10 + (n // 1000)
            if not visited[L]:
                visited[L] = True 
                reg.append([L,c+'L'])
            #R계산
            R = (n % 10) * 1000 + (n//10)
            if not visited[R]:
                visited[R] = True
                reg.append([R,c+'R'])
            
bfs()