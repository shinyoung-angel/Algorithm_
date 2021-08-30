
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]



    for i in range (N):
        for j in range(N):
            if arr[i][j] == 'A':
                for k in range(4):
                    nr = i + dr[k]
                    nc = j + dc[k]
                    if 0<= nr < N and 0 <= nc < N and arr[nr][nc] == 'H':
                        arr[nr][nc] = 'X'

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'B':
                for h in range(1, 3):
                    for k in range(4):
                        nr = i + dr[k] * h
                        nc = j + dc[k] * h
                        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'H':
                            arr[nr][nc] = 'X'

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'C':
                for h in range(1, 4):
                    for k in range(4):
                        nr = i + dr[k] * h
                        nc = j + dc[k] * h
                        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 'H':
                            arr[nr][nc] = 'X'

    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'H':
                cnt += 1

    print('#{} {}'.format(tc, cnt))

