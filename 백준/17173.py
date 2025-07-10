N,M = map(int,input().split()) #1 ~ N / M개 자연수 배수
lst = list(map(int,input().split()))
result = set()
for i in range(1,N+1):
    for j in lst:
        if i % j == 0:
            result.add(i)
print(sum(result))