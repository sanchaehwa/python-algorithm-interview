import sys
sys.setrecursionlimit(10**6)

#5 * 5 숫자판
graph = [list(map(int,sys.stdin.readline().split()))for _ in range(5)]
#가능한 6자리의 수를 구하는데 set을 써서 중복은 피하고 답을 구하도록
result = set()

def dfs(x,y,num,depth):

    if depth== 6:
        result.add(num)
        return
    #상하좌우
    dx = [0,0,1,-1]
    dy = [-1,1,0,0]
    
    for i in range(4):
        nx, ny = dx[i] + x , dy[i] + y
        #탐색 수 
        if 0 <= nx < 5 and 0 <= ny < 5:
            #문자열로 이어 붙이기
            dfs(nx,ny,num + str(graph[nx][ny]),depth+1)


#시작점 
for i in range(5):
    for j in range(5):
        dfs(i,j,str(graph[i][j]),1)
print(len(result))