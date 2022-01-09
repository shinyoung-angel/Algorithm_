import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))

low = 1
high = max(arr)

while low <= high:
    mid = (low+high) // 2
    cnt = 0
    for num in arr:
        cnt += num // mid

    if cnt < n:
        high = mid - 1
    else:
        low = mid + 1

print(high)
