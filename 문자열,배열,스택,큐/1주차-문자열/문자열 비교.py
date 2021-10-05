T = int(input())
for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    idx1, idx2 = 0, 0
    result = 0
    while idx1 < len(str1) and idx2 < len(str2):
        if str1[idx1] != str2[idx2]:
            idx2 = idx2 - idx1
            idx1 = -1
        idx1 += 1
        idx2 += 1
        if idx1 == len(str1):
            result = 1

    print('#{} {}'.format(tc, result))


#----------------------------------

for tc in range(1, int(input()) + 1):
    p = input()
    t = input()
    N = len(p)
    M = len(t)

    ans = 0

    for i in range(M - N + 1):
        if t[i: i+N] == p:
            ans = 1


    print('#{} {}'.format(tc, ans))
