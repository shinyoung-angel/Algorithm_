for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]

    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for j in range(r1, r2 + 1):
            for k in range(c1, c2 + 1):
                arr[j][k] += color

    result = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                result += 1

    print('#{} {}'.format(tc, result))