

for tc in range(1, int(input())+1):
    N = int(input())
    check = [0] * 26

    for i in range(N):

        test = input()
        check[ord(test[0])-65] = 1

    cnt = 1
    for i in range(1, 26):
        if check[0] == 1:
            if check[i] == 1:
                cnt += 1
            else:
                break
        else:
            cnt = 0
            break

    print('#{} {}'.format(tc, cnt))