

from collections import deque
import sys
#1. QueueStack을 구성하는 자료구조의 개수 N
N = int(sys.stdin.readline())
#길이 N의 수열 A = 어떤 자료구조인지
A = list(map(int,sys.stdin.readline().split()))
#길이 N의 수열 B = 각 자료구조마다 들어있는 원소
B = list(map(int,sys.stdin.readline().split()))
# lst = []
# for i in range(N):
#     if A[i] == 0: #큐
#         q1 = deque()
#         q1.append(B[i])
#         lst.append(q1)
#     else:
#         q2 = []
#         q2.append(B[i])
#         lst.append(q2)

M = int(sys.stdin.readline())
C = list(map(int,sys.stdin.readline().split()))
# result = deque() #시간복잡도 O(1)
# for i in C:
#     temp = i
#     for j in range(N):
#         if A[j] == 0:
#             lst[j].append(temp)
#             temp = lst[j].popleft()
#     result.append(temp)
queue = deque([])
for i in range(N):
    if A[i] == 0: # 큐인 자료구조만 모으기
        queue.append(B[i])

# 배열 C의 원소를 1개 appendleft 할 때마다 pop 연산 수행
for i in range(M):
    queue.appendleft(C[i])
    print(queue.pop(), end= ' ')


# print(' '.join(map(str,list(result))))

#구조1 ~ N개까지의 각각의 리스트
#각 자료구조를 담을 리스트
# lst = []
# for i in range(N):
#     if A[i] == 0: #큐
#         q1 = deque()
#         q1.append(B[i])
#         lst.append(q1)
#     else:
#         q2 = []
#         q2.append(B[i])
#         lst.append(q2)
# # N 자료구조에 원소 삽입하면 -- 기존에 있는 원소는 Pop -> 다음 자료구조에 들어감
# M = int(input())
# C = list(map(int,input().split()))
# result = []
# for i in C:
#     #첫번째 자료구조에는 i가 들어가고 
#     temp = i
#     for j in range(N):
#         if  A[j] == 0:
#             lst[j].append(temp) #원소삽입
#             temp = lst[j].popleft()

#         else:
#             lst[j].appendleft(temp)
#             temp = lst[j].pop()
#     result.append(temp)
# print(' '.join(map(str, result)))