

def check(s):

    word_dict = {}
    for alphabet in s:
        if not word_dict.get(alphabet):
            word_dict[alphabet] = 1
        else:
            word_dict[alphabet] += 1

    if len(word_dict) == 2:
        return 'Yes'
    else:
        return 'No'


for tc in range(1, int(input())+1):
    word = input()

    print('#{} {}'.format(tc, check(word)))