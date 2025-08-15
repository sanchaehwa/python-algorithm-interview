import sys
from collections import deque
class Solution:
    def snake(self)->int:
        N = int(sys.stdin.readline())
        #보드 이차원 6 *6 크기
        board = [[0] * N for _ in range(N)] #0으로 초기화된 보드판
        #사과 개수 
        K = int(sys.stdin.readline())
        for _ in range(K):
            x,y = map(int,sys.stdin.readline().split())
            board[x-1][y-1] = 1 #사과가 있는 위치는 1로 
        #오른쪽이면 +1 만큼 왼쪽 -1만큼 
        #뱀의 변환 횟수 : L
        turns = dict()
        L = int(sys.stdin.readline())
        for _ in range(L):
            m,c = map(str,sys.stdin.readline().split())
            turns[int(m)] = c
        #오른쪽 왼쪽 상하좌우
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        direction = 0
        snake = deque()
        snake.append((0,0))
        time = 0
        while True:
            time += 1
            head_x,head_y = snake[0]
            #이동방향
            nx = head_x + dx[direction]
            ny = head_y + dy[direction]
            if not (0 <= nx < N and 0 <= ny < N):
                break #벽에 부딪치면
            if (nx,ny) in snake:
                break #자기 자신
            snake.appendleft((nx,ny))
            if board[nx][ny] == 1: #사과가 있으면 꼬리 유지
                board[nx][ny] = 0 #사과 먹어서
            else:
                snake.pop()
            if time in turns: #방향을 바꾸기
                if turns[time] == "D" : #오른쪽 +1
                    direction = (direction + 1) % 4
                else: #왼쪽
                    direction = (direction -1) % 4
        print(time)

solution = Solution()
solution.snake()



                


