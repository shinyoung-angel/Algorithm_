import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

cnt = 1
dp = [[0]*(m+1) for _ in range(n+1)]
nx, ny = 0, 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if cnt == k:
            nx, ny = i, j
        if i == 1 or j == 1:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
        cnt += 1

if k == 0:
    print(dp[n][m])
else:
    print(dp[nx][ny] * dp[n-nx+1][m-ny+1])

