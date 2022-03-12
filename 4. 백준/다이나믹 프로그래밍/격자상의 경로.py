import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
# n, m, k = 7, 11, 76
def calc (x, y):
    dp = [[0]*y for _ in range(x)]

    for i in range(x):
        for j in range(y):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

    return dp[x-1][y-1]

if k == 0:
    print(calc(n, m))
else:
    row = k // m
    col = k - (row*m) - 1
    first = calc(row+1, col+1)
    second = calc(n-row, m-col)
    print(first*second)
