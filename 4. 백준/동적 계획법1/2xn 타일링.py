import sys
input = sys.stdin.readline

num = int(input())
dp = [0] * (num+1)

if num <= 2: print(num)
else:
    dp[1] = 1
    dp[2] = 2
    for i in range(3, num+1):
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[num] % 10007)

## 재귀는 런타임 에러 및 시간 초과~~~
# def fibo(n):
#
#     if n == 1: return 1
#     elif n == 2: return 2
#     else: return fibo(n-1) + fibo(n-2)
#
# print(fibo(num)%10007)

