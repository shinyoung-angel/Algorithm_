

import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.insert(0, [0, 0])
dp = [0] * (n+2)

for i in range(n, 0, -1):
    if i + arr[i][0] > n+1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], arr[i][1] + dp[i+arr[i][0]])

print(dp[1])

########################

def counseling(idx=0, pay=0):
    global ans

    for i in range(idx, N):
        if i + test_case[i][0] < N+1:
            counseling(i + test_case[i][0], pay + test_case[i][1])
    if ans < pay:
        ans = pay
    return


N = int(input().strip())

test_case = [list(map(int, input().strip().split())) for _ in range(N)]

ans = 0
counseling()
print(ans)