
import collections
from collections import deque

#pop(0) = O(n) -- 데크(양쪽 끝에서 추가,삭제,조회할 수 있는) popleft() --O(1)

s = input() #문자열 입력

def solution(s):
    #데크
    strs: deque = collections.deque()
    for char in s:
        if char.isalnum(): #문자, 숫자인 경우
            strs.append(char.lower()) #소문자로 변환해서 추가
    while len(strs)>1:
        if strs.popleft() != strs.pop():
            return False
    return True
print(solution(s)) 
