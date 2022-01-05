dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

def bfs(start_row, start_col):

    q = [(start_row, start_col)]
    visited[start_row][start_col] = 1

    while q:

        row, col = q.pop(0)

        if arr[row][col] == 3:
            return visited[row][col] - 2

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue

            if (arr[nr][nc] == 0 or arr[nr][nc] == 3) and visited[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = visited[row][col] + 1
    return 0


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start_row = i
                start_col = j

    print('#{} {}'.format(tc, bfs(start_row, start_col)))



