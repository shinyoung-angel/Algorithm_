



for tc in range(1, int(input())+1):
    n = float(input())

    binary = ''
    for i in range(1, 13):
        square = 2 ** (-i)

        if n >= square:
            n -= square
            binary += '1'

        else:
            binary += '0'

        if n == 0:
            print('#{} {}'.format(tc, binary))
            break

    else:
        print('#{} {}'.format(tc, 'overflow'))



