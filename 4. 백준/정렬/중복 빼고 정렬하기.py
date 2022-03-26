
import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
arr = set(arr)
arr = list(arr)
arr.sort()

print(*arr)
