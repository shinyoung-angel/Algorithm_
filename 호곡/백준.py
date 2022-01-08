
import sys
input = sys.stdin.readline


n = int(input())
m = int(input())
if m != 0:
    arr = list(map(int, input().split()))
else:
    arr = []

ans = abs(n-100)

for i in range(1000001):
    for j in str(i):
        if int(j) in arr:
            break
    else:
        ans = min(ans, len(str(i)) + abs(n-i))

print(ans)