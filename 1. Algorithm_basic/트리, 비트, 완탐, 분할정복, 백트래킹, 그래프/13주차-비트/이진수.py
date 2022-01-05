


for tc in range(1, int(input())+1):
    n, hexa = input().split()

    word = ''

    ## 16진수 --> 10진수 --> 2진수
    for i in hexa:
        word += format(int(i, 16), '04b')

    # ####
    # for i in range(int(n)):
    #     word += '{:04b}'.format(int(hexa[i], 16))

    print('#{} {}'.format(tc, word))