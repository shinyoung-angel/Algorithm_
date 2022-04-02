
import sys
input = sys.stdin.readline

arr = [[0]*101 for _ in range(101)]
ans = 0
for _ in range(4):
    a, b, c, d = map(int,input().split())

    for i in range(b, d):
        for j in range(a, c):
            arr[i][j] += 1
            if arr[i][j] == 1:
                ans += 1

print(ans)

