import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0 and j != 0:
            arr[i][j] += arr[i][j-1]
        elif j == 0 and i != 0:
            arr[i][j] += arr[i-1][j]
        else:
            arr[i][j] += arr[i-1][j] + arr[i][j-1]

print(arr)
for _ in range(m):
    a, b, c, d = map(int, input().split())
    print(arr[c-1][d-1]-arr[a-1][b-1])