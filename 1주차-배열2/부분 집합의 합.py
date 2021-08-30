
for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    result = 0

    for i in range(1<<12):
        cnt = 0
        total = 0
        for j in range(12):
            if i & (1 << j):
                cnt += 1
                total += A[j]

        if cnt == N and total == K:
            result += 1

    print('#{} {}'.format(tc, result))
