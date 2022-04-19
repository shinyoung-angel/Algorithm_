import sys
input = sys.stdin.readline

n = int(input())
wine = [0]
for _ in range(n):
    tmp = int(input())
    wine.append(tmp)

dp = [0] * (n+1)
dp[1] = wine[1]

for i in range(2, n+1):
    dp[i] = max(dp[i-1], dp[i-2]+wine[i], dp[i-3]+wine[i-1]+wine[i])

print(dp[n])



