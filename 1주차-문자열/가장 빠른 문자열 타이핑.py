for tc in range(1, int(input()) + 1):
    str1, str2 = list(input().split())

    large = len(str1)
    small = len(str2)

    i = 0
    cnt = 0
    ans = 0
    idx = 0

    while i < large - small + 1:

        if str1[i: i+small] == str2:
            cnt += 1
            i += small
        else:
            i += 1

    ans = large - cnt * small + cnt

    print('#{} {}'.format(tc, ans))

# ---------------------------

# T = int(input())
# for tc in range(1, T+ 1):
#     a, b = input().split()
#
#     idx = 0
#     cnt = 0
#
#     while idx < len(a) - len(b) + 1:
#         if a[idx:idx + len(b)] == b:
#             idx += len(b)
#             cnt += 1
#         else:
#             idx += 1
#
#     result = len(a) - (len(b) - 1) * cnt
#     print('#{} {}'.format(tc, result))
