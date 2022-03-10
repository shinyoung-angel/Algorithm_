import sys
input = sys.stdin.readline

n = int(input())

ans = []

arr = [list(map(int, input().split())) for _ in range(n)]

### 둘째줄부터 위에 있는 아이들 중 최소값을 더해주기
for i in range(1, n):
    arr[i][0] += min(arr[i-1][1], arr[i-1][2])
    arr[i][1] += min(arr[i-1][0], arr[i-1][2])
    arr[i][2] += min(arr[i-1][1], arr[i-1][0])

print(min(arr[n-1]))