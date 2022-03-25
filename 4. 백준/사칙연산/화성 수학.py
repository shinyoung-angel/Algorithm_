import sys
input = sys.stdin.readline

for _ in range(int(input())):
    mars = list(input().strip().split())
    num = float(mars[0])

    for i in range(1, len(mars)):
        tmp = mars[i]

        if tmp == '@':
            num *= 3
        elif tmp == '%':
            num += 5
        else:
            num -= 7

    print('{:.2f}'.format(num))