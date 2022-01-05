
n = int(input())

for _ in range(n):
    word = input()
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:]:
                n -= 1
                break

print(n)

# --------------------------------
# 틀림 왜,,,??????????
ans = 0
for tc in range(int(input())):
    word = input()
    # 첨에 단어 첫 글자를 담아 놓고 췤
    check = [word[0]]
    cnt = 0

    # 첫 글자 담아 놨으니 1부터 시좍
    for i in range(1, len(word)):

        # 인덱스 에러 데비 try-except
        try:

            # 앞앞까지 겹치는 아이가 없다면 cnt += 1
            if (word[i] == check[-1] or word[i] != check[-1]) and word[i] not in word[:i-1]:
                cnt += 1

            # 겹친다면 0 하고 브레잌
            else:
                cnt = 0
                break

        except:
            cnt += 1

    if cnt == len(word) - 1:
        ans += 1

print(ans)


