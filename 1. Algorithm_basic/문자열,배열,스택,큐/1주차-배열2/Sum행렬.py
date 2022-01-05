# Sum 열, 대각선, 행
-----------------------------------------

for tc in range(1, 11):
    N = int(input())
    TC = [list(map(int, input().split())) for _ in range(100)]
    max_value = 0


    for i in range(100):
        ans = 0
        for k in range(100):
            ans += TC[i][k]
        if ans > max_value:
            max_value = ans

    for i in range(100):
        ans = 0
        for k in range(100):
            ans += TC[k][i]
        if ans > max_value:
            max_value = ans
    ans = 0
    for i in range(100):
        ans += TC[i][i]
        if ans > max_value:
            max_value = ans
    ans = 0
    for i in range(100):
        ans += TC[i][99-i]
        if ans > max_value:
            max_value = ans

    print('#{} {}'.format(tc, max_value))

-------------------------------------
def maxmax(hi):
    max_value = 0
    for i in hi:
        if i > max_value:
            max_value = i
    return max_value

for tc in range(1, 11):
    N = int(input())
    TC = [list(map(int, input().split())) for _ in range(100)]

    ans = 0

    for i in range(100):
        i_total = 0
        j_total = 0
        cross = 0
        cross2 = 0

        for j in range(100):
            i_total += TC[i][j]
            j_total += TC[j][i]

            if i == j:
                cross += TC[i][j]

            elif i + j == 99:
                cross2 += TC[i][j]


        if i_total > ans:
            ans = i_total
        if j_total > ans:
            ans = j_total
        if cross > ans:
            ans = cross
        if cross2 > ans:
            ans = cross2

    print('#{} {}'.format(tc, ans))



