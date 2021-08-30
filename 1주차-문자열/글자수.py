


for tc in range(1, int(input()) + 1):
    str1 = input()
    str2 = input()
    max_value = 0

    for i in str1:
        cnt = 0
        for j in str2:
            if i == j:
                cnt += 1
        if cnt > max_value:
            max_value = cnt

    print('#{} {}'.format(tc, max_value))