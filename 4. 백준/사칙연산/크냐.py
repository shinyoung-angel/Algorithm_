
import sys
input = sys.stdin.readline

for _ in range(10000000000000000000000000000000000):
    a, b = map(int, input().split())
    if a == 0 and b == 0: break

    elif a> b: print('Yes')
    else: print('No')