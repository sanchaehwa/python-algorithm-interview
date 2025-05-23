#사용자로부터 입력 input()/ input() => 문자열을 입력받는 함수 
#1 4 이렇게 두개의 숫자 사이에는 공백이 포함되어 있기에, 공백기준으로 문자열을 split 하고 int형으로 출력만

#2557.py
A,B = input().split( ) #Split 공백을 기준으로 자르는것
print(int(A)+int(B))
#2558.py
print(int(A)-int(B))
#10998.py
print(int(A) * int(B))
#10926.py

#10926 문제는 단순 출력
id = input()
print(id +"??!")

#18108 불기연도 = 서기 연도 + 543 / 서기연도 = 불기연도 - 543
#불기연도
y = input()
print(int(y) - 543)
#10430.py 
#공백 기준으로 입려받은 값을 바로 int 형으로 바꿈
A,B,C = map(int,input().split())
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)