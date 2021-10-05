
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs ():

    q = [(start_row, start_col)]
    visited[start_row][start_col] = 1

    while q:

        row, col = q.pop(0)

        if arr[row][col] == 3:
            return 1

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if nr < 0 or nr >= 16 or nc < 0 or nc >= 16: continue

            if (arr[nr][nc] == 0 or arr[nr][nc] == 3) and visited[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = 1
    return 0


for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                start_row = i
                start_col = j


    print('#{} {}'.format(tc, bfs()))