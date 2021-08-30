for tc in range(1, 11):
    N = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    r = 99
    c = 0
    for i in range(100):
        if ladder[99][i] == 2:
            c = i


    while True:

        if 0 < c < 100 and ladder[r][c - 1] == 1:  # 왼쪽이 1일때 까지 column에서 1을 빼기 이후 row에서 1을 빼기
            while 0 < c < 99 and ladder[r][c - 1] == 1:
                c -= 1
            else:
                r -= 1



        elif 0 < c < 99 and ladder[r][c + 1] == 1:
            while 0 < c < 99 and ladder[r][c + 1] == 1:
                c += 1
            else:
                r -= 1


        else:
            r -= 1

        if r == 0:
            break

    print('#{} {}'.format(tc, c))

# -------------------------------------------------------- #

for tc in range(1, 11):
    N = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    r = 99
    c = 0

    for i in range(100):
        if ladder[r][i] == 2:
            c = i

    while True:

        if r == 0:
            break

        if 0 < c and ladder[r][c-1] == 1:
            while 0 < c and ladder[r][c-1] == 1:
                c -= 1

        elif c < 99 and ladder[r][c+1] == 1:
            while c < 99 and ladder[r][c+1] == 1:
                c += 1

        else:
            r -= 1

    print('#{} {}'.format(tc, c))

