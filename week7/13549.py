import sys
from collections import deque
input = sys.stdin.readline
# N ==> 혅재 언니의 위치 / K ==> 동생의 위치 * N에서 K 까지 가는 가장 빠른 시간을 출력
N,K = map(int,input().split())

def find(N,K):
    #100,000
    MAX = 100000
    INF = int(1e9) #아주 큰 수로 초기화
    dist = [INF] * (MAX+1) #시간을 담을 
    dq = deque()
    dist[N] = 0 #시작위치의 가중치 - 0
    dq.append(N) #[5]

    while dq:
        current = dq.popleft()
        if current == k:
            return dist[current]
        if 