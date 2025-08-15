
import sys
input = sys.stdin.readline

# 피보나치 재귀에서 fib(1) 또는 fib(2) return이 몇 번 일어나는지 세기
cnt1 = 0
def fib(n):
    global cnt1
    if n == 1 or n == 2:
        cnt1 += 1
        return 1
    return fib(n-1) + fib(n-2)

# 반복문에서 계산 횟수 세기
def fibonacci(n):
    cnt2 = 0
    dp = [0] * (n+1)
    dp[1] = dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        cnt2 += 1
    return cnt2

N = int(input())
fib(N)
print(cnt1, fibonacci(N))

############
import sys
input = sys.stdin.readline
def fibonacci(n):
    dp = [0] * (n+1)
    dp[1] = dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n], n-2  # 첫 번째는 fib(1)/fib(2) 호출 횟수, 두 번째는 반복문 실행 횟수

N = int(input())
a, b = fibonacci(N)
print(a, b)