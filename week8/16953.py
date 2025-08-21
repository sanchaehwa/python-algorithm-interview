import sys
from collections import deque
input = sys.stdin.readline


'''
1. cnt : 연산 횟수 
- B를 2로 나누었을때 나머지가 0아면 Q를 pop 해서 나온수에 2를 더한다음에 넣고 
- B를 1로 나누었을때 나머지가 1이면 1를 뒤에 붙이고
- Q의 값이 결국 B가 되었을때 이제 연산 종료하고 +1
- Q의 길이

'''
A,B = map(int,input().split())

def bfs(a):
    q = deque()
    q.append((a,1))
    while q:
        num,cnt = q.popleft()
        if num == B:
            print(cnt)
            return
        #연산이 가능한 경우를 다 해보는 로직
        if 2 * num <= B : #2로 나누었을때 나머지가 0이면 -> 2씩 더하는 수가 B보다 작거나 같은 경우에는 연산이 가능함
            q.append((num*2,cnt+1))
        if 10 * num + 1 <= B: 
            q.append((num*10+1,cnt+1))
    print(-1)


bfs(A)