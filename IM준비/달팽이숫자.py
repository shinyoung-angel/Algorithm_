
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, int(input())+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    r = c = d = 0
    num = 1

    while num <= N * N:

        arr[r][c] = num
        num += 1

        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            r, c = nr, nc
        else:
            d = (d+1) % 4
            r += dr[d]
            c += dc[d]


    print('#{}'.format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()

