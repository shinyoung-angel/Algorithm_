
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    tmp = input().strip()
    print(tmp[0].upper(), end='')
    print(tmp[1:])