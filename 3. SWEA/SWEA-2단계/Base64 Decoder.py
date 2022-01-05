


from base64 import b64decode

for tc in range(1, int(input()) + 1):

    word = input()
    res = b64decode(word).decode('UTF-8')

    print('#{} {}'.format(tc ,res))