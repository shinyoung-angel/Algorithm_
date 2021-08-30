

for tc in range(1, int(input())+1):
    test = list(input())
    original = ['0'] * len(test)
    cnt = 0

    for i in range(len(test)):
        if test[i] != original[i]:
            original[i:] = test[i] * len(test[i:])
            cnt += 1

    print('#{} {}'.format(tc, cnt))

        
