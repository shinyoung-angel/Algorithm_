T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    c = [0] * 12

    for i in range(6):
        c[N % 10] += 1
        N //= 10

    i = 0
    tri_num = run_num = 0

    while i < 10:
        if c[i] >= 3:
            c[i] -= 3
            tri_num += 1
            continue
        if c[i] >= 1 and c[i + 1] >= 1 and c[i + 2] >= 1:
            c[i] -= 1
            c[i + 1] -= 1
            c[i + 2] -= 1
            run_num += 1
            continue
        i += 1

    if run_num + tri_num == 2:
        print('#{} {}'.format(tc, '1'))
    else:
        print('#{} {}'.format(tc, '0'))

