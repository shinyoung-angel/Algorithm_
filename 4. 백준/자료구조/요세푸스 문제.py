
import sys
input = sys.stdin.readline


n, k = map(int, input().split())
arr = list(i for i in range(1, n+1))
result = []
pick = k

while arr:

    pick = (pick-1) % len(arr)
    result.append(arr[pick])
    arr.pop(pick)
    pick += k

print('<', end='')
for i in range(n):
    if i == n-1:
        print(result[i], end='')
    else:
        print(result[i], end=', ')
print('>')





