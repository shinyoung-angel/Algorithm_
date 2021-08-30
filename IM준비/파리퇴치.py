

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            ans = 0
            for k in range(M):
                for h in range(M):
                    ans += arr[i+k][j+h]
            if ans > max_value:
                max_value = ans

    print('#{} {}'.format(tc, max_value))
