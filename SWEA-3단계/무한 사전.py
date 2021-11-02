

for tc in range(1, int(input())+1):
    word1 = input()
    word2 = input()

    result = 'N'

    for i in word1:
        if i not in word2:
            result = 'Y'

    for i in word2:
        if i not in word1:
            result = 'Y'


    print('#{} {}'.format(tc, result))