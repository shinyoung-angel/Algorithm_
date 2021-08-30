
# 허락을 받고 하자
for tc in range(1, int(input())+1):
    word = [0] * 5

    max_len = 0

    for i in range(5):
        word[i] = list(input())
        if len(word[i]) > max_len:
            max_len = len(word[i])

    print('#{}'.format(tc), end=" ")

    for i in range(max_len):
        for j in range(5):
            if len(word[j]) > i:
                print(word[j][i], end ="")

    print()

# --------------------------

# 허락 ㄴㄴ 용서 ㄱㄱ
for tc in range(1, int(input())+1):

    word = [0] * 5
    max_len = 0

    for i in range(5):
        word[i] = list(input())
        if len(word[i]) > max_len:
            max_len = len(word[i])


    print('#{}'.format(tc), end= ' ')

    for i in range(max_len):
        for j in range(5):

            try:
                print(word[j][i], end='')

            except:
                pass

    print()


