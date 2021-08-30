for tc in range(1, int(input()) + 1):
    N, M = list(map(int, input().split()))
    c = [list(input()) for _ in range(N)]

    ans = []
    for i in range(N):
        for k in range(N-M+1):
            if c[i][k: k+M] == c[i][k: k+M][::-1]:
                ans.append(''.join(c[i][k:k+M]))


    for k in range(N):
        for i in range(N-M+1):
            new = []
            for j in range(M):
                new.append(c[i+j][k])
            if new == new[::-1]:
                ans.append(''.join(new))


    print('#{} {}'.format(tc, *ans))