
def binary(page, key):
    start = 1
    end = page
    cnt = 0

    while start <= end:
        middle = (start+end) // 2
        cnt += 1
        if middle == key:
            return cnt
        elif middle > key:
            end = middle
        else:
            start = middle


for tc in range(1, int(input())+1):
    pages, A_find, B_find = map(int, input().split())

    cnt_A = binary(pages, A_find)
    cnt_B = binary(pages, B_find)
    ans = ''


    if cnt_A > cnt_B:
        ans = 'B'
    elif cnt_A < cnt_B:
        ans = 'A'
    else:
        ans = 0


    print('#{} {}'.format(tc, ans))







