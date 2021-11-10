import sys
input = sys.stdin.readline

n = int(input())

ans = []

arr = [list(map(int, input().split())) for _ in range(n)]

for j in range(3):
    result = arr[0][j]
    idx = j
    for i in range(1, n):
        if idx == 0:
            value = min(arr[i][1], arr[i][2])

        elif idx == 1:
            value = min(arr[i][0], arr[i][2])

        elif idx == 2:
            value = min(arr[i][0], arr[i][1])

        idx = arr[i].index(value)
        result += value
    ans.append(result)

print(min(ans))