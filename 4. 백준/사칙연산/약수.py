import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))
arr.sort()

if n == 1:
    print(arr[0] * arr[0])
else:
    print(arr[0]*arr[-1])