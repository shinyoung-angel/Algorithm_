

for tc in range(1, int(input())+1):
    word1 = input().strip()
    word2 = input().strip()


    result = 'Y'

    if word1 == word2[:len(word2)-1] and word2[-1] == 'a':
        result = 'N'

    print('#{} {}'.format(tc, result))