import sys
input = sys.stdin.readline
from collections import Counter
'''
1. 문자열을 돌면서 i가 있는지 그 문자가 있는지 있으면 count하고 count가 가장 많은 문자를 고르는 경우
2. Dict 써서 A : - U : - C : - 
3. Key 값이 같은 것을 찾고 str += alphabet (같은 모든 것을 문자열에 포함하면 - 가장 긴 부분 문자열 )
'''
input1 = input().strip()
input2 = input().strip()

#input1을 담을 dict
dict1 = Counter(input1)
#input2를 담을 dict
dict2 = Counter(input2)

password = "" 

for key in dict1:
    if key in dict2:
        password += key
print(password)
