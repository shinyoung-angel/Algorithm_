

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    Y, K = 0, 0
    for _ in range(9):
        a, b = map(int, input().split())
        Y += a
        K += b

    if Y > K: print('Yonsei')
    elif Y < K: print('Korea')
    else: print('Draw')
