def solution(n:int,m:int)->list:
    basket = [i for i in range(1,n+1)]
    temp = 0
    for x in range(m):
        i,j = map(int,input().split())
        temp = basket[i-1:j]
        temp.reverse()
        basket[i-1:j] = temp
    for x in range(n):
        print(basket[x],end=" ") #한줄에 여러 숫자를 출력할수있음

n,m = map(int,input().split())
#한줄에 여러개,그런걸 n줄 입력 받을때
# lst = [list(map(int,input().split())) for _ in range(basket[1])]
solution(n,m)