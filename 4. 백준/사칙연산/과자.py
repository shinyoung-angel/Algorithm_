import sys
input = sys.stdin.readline

k, n, m = map(int, input().split())
result = k*n-m
print(result if result >= 0 else 0)