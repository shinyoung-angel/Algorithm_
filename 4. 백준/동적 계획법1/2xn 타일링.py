import sys
input = sys.stdin.readline

num = int(input())

## 재귀는 런타임 에러 및 시간 초과~~~
# def fibo(n):
#
#     if n == 1: return 1
#     elif n == 2: return 2
#     else: return fibo(n-1) + fibo(n-2)
#
# print(fibo(num)%10007)

dp = [0] * 1001
dp[0], dp[1] = 1, 2

if num == 1: print(1)
elif num == 2: print(2)
else:
    for i in range(2, num):
        dp[i] = dp[i-1] + dp[i-2]
print(dp[num-1]%10007)