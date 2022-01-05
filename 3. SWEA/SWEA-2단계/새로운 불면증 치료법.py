


for tc in range(1, int(input())+1):
    n = int(input())

    check = [0] * 10
    i = 0

    while True:

        if 0 not in check:
            break

        i += 1
        num = i * n

        for j in str(num):
            check[int(j)] = 1

    print('#{} {}'.format(tc, num))

