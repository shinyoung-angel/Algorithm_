


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))

    q = []
    for i in range(N):
        q.append([cheese[i], i])

    i = 0
    while len(q) > 1:
        q[0][0] //= 2

        if q[0][0] == 0:
            if N+i < M:
                q.pop(0)
                q.append([cheese[N+i], N+i])
                i += 1
            elif N+i >= M:
                q.pop(0)

        else:
            q.append(q.pop(0))

    print('#{} {}'.format(tc, q[0][1]+1))