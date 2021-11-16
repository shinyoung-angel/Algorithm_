

for tc in range(1, int(input())+1):
    n = int(input())
    week = list(map(int, input().split())) * 100000

    for idx in range(7):
        if week[idx] == 1:
            start = idx
            break

    cnt = 0
    result = 0

    for idx in range(start, 7000000):
        i = week[idx]
        if i == 1:
            cnt += 1
            if cnt == n:
                result = idx + 1 - start
                break


    print('#{} {}'.format(tc, result))




