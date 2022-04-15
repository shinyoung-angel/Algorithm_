word = input()
len_word = len(word)
cnt = 0

while True:

    if len_word > cnt:
        print(word[cnt:cnt+10])

    else:
        print(word[cnt:])
        break

    cnt += 10