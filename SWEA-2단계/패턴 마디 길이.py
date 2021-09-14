

for tc in range(1, int(input())+1):
    word = input()

# 각 문자열의 길이가 30이고 마디의 최대 길이가 10이니까
    # 길이가 10 이내로 마디를 찾음. 찾으면 break하고 길이 잰다.
    for i in range(1,11):
        if word[:i] == word[i:2*i]:
            ans = word[:i]
            break

    print('#{} {}'.format(tc, len(ans)))
