'''
-> 길이가 2인경우
- S에 x가 이미 있는 경우는 연산을 무시한다 => 같은 숫자르 중복해서 넣지않는다
* 중복을 허용하지 않는 SET을 사용 해야한다.
- S에 x를 제거 -> 없는 경우는 무시한다 => set(),discard()
- in : if x in temp 
- 명령어의 길이가 1인경우는 => All * 1 부터 20으로 바꾼다는거 

'''
import sys
input = sys.stdin.readline

N = int(input())
S = set()
for _ in range(N):
    temp = input().strip().split()
    if len(temp) == 1:
        if temp[0] == "all":
            S = set([i for i in range(1,21)])
        else: #empty
            S = set()
    
    else: #길이가 2인 경우
        cmd,num = temp[0],temp[1]
        # str --> int
        num = int(num)
        if cmd == "add":
            S.add(num)
        if cmd == "check":
            print(1 if num in S else 0 )
        if cmd == "remove":
            S.discard(num)
        if cmd == "toggle":
            if num in S: #S에 x가 있는 경우
                S.discard(num)
            else: #S에 X가 없는 경우
                S.add(num)
        