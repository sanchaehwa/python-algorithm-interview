import sys
input = sys.stdin.readline

N,M = map(int,input().split())
visited = [False] * (N+1)
rs = [] 

def recur(num,depth):
    if depth == M:
        print(' '.join(map(str,rs)))
        return
    for i in range(num,N+1): #num은 반복문의 시작값 ---
        if visited[i] == False:
            visited[i] = True
            rs.append(i)
            recur(i+1,depth+1) #현재 고른 숫자 i보다 더 큰 수를 선택해야함
            visited[i] = False
            rs.pop()
recur(1,0)