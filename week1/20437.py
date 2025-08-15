#딕셔너리 - Key: 문자 ,Value: 문자의 인덱스
#Value가 입력값2번째랑 같으면 해당 인덱스까지 슬라이싱 
#마지막 위치 - 처음위치 + 1
# t = int(input())
# for _ in range(t):
#     w = input()
#     k = int(input())
#     word = {}
#     for i in range(len(w)):
#         if word.get(w[i]):
#                 word[w[i]].append(i)
#         else: #새로운 원소
#                 word[w[i]] = [i]
#     for value in word.values():
#         print(value)
#         n = len(value)
#         if n >= k: #각 문자가 K개 이상 존재해야하니깐
#             for s in range(n-k+1):
#                 cmd = 

#         else:
#             print(-1)

import sys
from collections import defaultdict
def solution(w:str, k:int)->int:
    if k == 1:
        return 1,1
    else:
        length = len(w)
        minLength = length 
        maxLength = 0
        word_dict = defaultdict(list)
        for j in range(length): #인덱스
            if w.count(w[j]) >= k:
                word_dict[w[j]].append(j)
        if not word_dict: 
            return -1,
        for a in word_dict.values():
            print(len(a))
            for b in range(len(a) - k+1): #슬라이싱
                target = a[b+k-1]-a[b]+1
                if target > maxLength:
                    maxLength = target
                if target < minLength:
                    minLength = target
        return minLength,maxLength

#w,k 초기화
T = int(input()) #게임수
w = [''] * T
k = [0] * T
for i in range(T):
    w[i] = input()
    k[i] = int(input())
for i in range(T):
    print(*solution(w[i],k[i]))