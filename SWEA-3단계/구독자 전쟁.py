

for tc in range(1, int(input())+1):
    n, a, b = map(int, input().split())
    minimum = 0

    if a+b > n:
        minimum = a+b-n

    maximum = min(a, b)
    print('#{} {} {}'.format(tc, maximum, minimum))

