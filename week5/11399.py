import sys
input = sys.stdin.readline


#사람의 수
N = int(input())
#돈을 인출하는데 걸리는시간 Pi
time = list(map(int,input().split()))
#큰수부터 처리를 해야하는것인가 -> 작은거부터 우선 처리하기
#오름 차순 정렬
time.sort()
#sum
sumTime = 0
#acc
acc = 0
for t in time:
    acc += t
    sumTime += acc
print(sumTime) 