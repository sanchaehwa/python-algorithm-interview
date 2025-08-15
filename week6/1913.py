import sys
input = sys.stdin.readline

N = int(input()) #7*7
num = int(input()) #35 찾아야하고

'''
달팽이 모양 -- 중간부터 시작해야해
END = (0,0)
START = (N // 2,N//2)
'''
start =  N//2

sprial_dy = [-1,0,1,0]
sprial_dx = [0,1,0,-1]
y,x = start,start
sprial_d = 0 #현재 방향 인덱스 방향이 바뀌면 0 -- 1로
cnt_max = 1
cnt = 0
change = 0
result = None
graph = [[0] * N for _ in range(N)]
graph[start][start] = 1
if num == 1:
    result = (start,start)

#다시
i = 2  
while True:
    if i > N*N:
        break
    y += sprial_dy[sprial_d] 
    x += sprial_dx[sprial_d]
    graph[y][x] = i
    if num == i:
        result = (y,x)
    i += 1
    cnt += 1
    if cnt == cnt_max:
        cnt = 0
        sprial_d = (sprial_d + 1) % 4
        change +=1
        if change == 2:
            change = 0
            cnt_max += 1

for i in graph:
    print(' '.join(map(str,i)))
print(result[0] +1, result[1]+1)