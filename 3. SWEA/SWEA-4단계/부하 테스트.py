import math

for tc in range(1, int(input())+1):
    l, p, c = map(int, input().split())

    cnt = 1
    tmp = l * c
    while tmp < p:
        cnt += 1
        tmp *= c

    print('#{} {}'.format(tc, math.ceil(math.log2(cnt))))
