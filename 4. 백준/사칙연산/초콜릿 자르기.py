import sys
input = sys.stdin.readline



## 간단해 보였는데 꽤 어렵군?
n, m = map(int, input().split())

result = (n-1) + n*(m-1)

print(result)