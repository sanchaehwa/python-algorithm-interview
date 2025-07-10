import sys

N,M = map(int,sys.stdin.readline().split())
graph = [list(sys.stdin.readline().strip()) for _ in range(N)]
min_cnt = float('inf')
for i in range(N-7):
    for j in range(M-7):
        cnt1,cnt2 = 0,0
        for y in range(i, i+8):
            for x in range(j, j+8):
                current = graph[y][x]
                if (x+y) % 2 == 0:
                    if current != 'W': #W 부터 시작
                        cnt1 += 1
                    if current != 'B':
                        cnt2 += 1
                else:
                    if current != 'B': #
                        cnt1 += 1
                    if current != 'W':
                        cnt2 += 1
        min_cnt = min(min_cnt,cnt2,cnt1)
print(min_cnt)
