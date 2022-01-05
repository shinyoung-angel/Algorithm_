
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]

    r = 0
    c = 0
    d = 0
    num = 1

    while num <= n * n:

        arr[r][c] = num
        num += 1

        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 0:
            r, c = nr, nc
        else:
            d = (d+1) % 4
            r += dr[d]
            c += dc[d]

    print('#{}'.format(tc))

    for i in range(n):
        print(*arr[i])




