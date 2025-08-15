import sys
input = sys.stdin.readline


cnt = 0
N,M = map(int,input().split())
graph = [list(input().strip()) for _ in range(N)]
min_cnt = float('inf')
#홀수번째 [W,B,W,B,W,B,W,B]
#짝수번째 [B,W,B,W,B,W,B,W]
for i in range(N-7):
    for j in range(M-7):
        cnt1,cnt2 = 0,0 #
        for n in range(i,i+8):
            for m in range(j,j+8):
                #현재위치
                current = graph[n][m]
                #if n이 홀수일때
                if (n+m) % 2 == 1:
                    if current != 'W':
                        cnt1 += 1
                    if current != 'B':
                        cnt2 += 1
                else:
                    if current != 'B':
                        cnt1 += 1
                    if current != 'W':
                        cnt2 += 1
        min_cnt = min(min_cnt,cnt1,cnt2)
print(min_cnt)
                    
