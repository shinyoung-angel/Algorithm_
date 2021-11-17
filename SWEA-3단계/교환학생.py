
for tc in range(1, int(input() ) +1):
    n = int(input())
    week = list(map(int, input().split()))

    result = 123456789

    for i in range(7):
        if week[i] == 1:
            idx = i
            cnt = 0
            day = 0
            while cnt < n:
                cnt += week[idx]
                idx = (idx +1) % 7
                day += 1

            if result > day:
                result = day

    print('#{} {}'.format(tc, result))
