#Ax + By + C = 0 -Ax + By + C = 0
#절댓값함수 : abs()
def solution(line):
    stars = set()
    for i in range(len(line)):
        #대칭성을 가지고 있다는것
        #x = (B1 * C2 - B2 * C1) / (A1 * B2 - A2 * B1) -> 분모가 0이면 평행
        #y = (C1 * A2 - C2 * A1) / (A1 * B2 - A2 * B1)
        for j in range(i+1, len(line)):
            A1,B1,C1 = line[i]
            A2,B2,C2 = line[j]
            denominator = A1 * B2 - A2 * B1
            if denominator == 0: #평행조건
                continue
            x_numer = B1 * C2 - B2 * C1
            y_numer = C1 * A2 - C2 * A1

            if x_numer % denominator != 0 or y_numer % denominator != 0: #정수가 아닌 조건
                continue
            x = x_numer // denominator
            y = y_numer // denominator
            stars.add((x,y))
    #좌표를 구해야해
    min_x = min(x for x,y in stars)
    max_x = max(x for x,y in stars)
    min_y = min(y for x,y in stars)
    max_y = max(y for x,y in stars)
    width = max_x - min_x + 1
    height = max_y - min_y + 1
    graph = [['.'] * width for _ in range(height)]
    for x,y in stars:
        row = max_y -y
        col = x - min_x
        graph[row][col] = '*'
    for g in graph:
        print(''.join(g))
line = [[2,-1,4],[-2,-1,4],[0,-1,1],[5,-8,-12],[5,8,12]]
solution(line)