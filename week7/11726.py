import sys
input = sys.stdin.readline
'''
1. DP : 이전의 값을 활용해서 문제를 풀어나가는것 -> 규칙을 찾는것이 중요
2. An = An-1 + An-2 이전의 값들을 더하면 현재 값이 나오는 점화식
3. 직사각형을 채우는 방법의 수 / 10007
'''
# n = 2 A1 + A0 /
# n = 5 A4 + A3 = A3+ A2 + A2 + A1 = A1 + A2 + A1 + A0 + A1 =

n = int(input())
rs = [0,1,2]

for i in range(3,n+1):
    rs.append((rs[i-1] + rs[i-2])%10007)
print(rs[n])