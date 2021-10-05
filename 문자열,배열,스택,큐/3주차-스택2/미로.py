dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def check(arr, start_r, start_c):
    stack = [[start_r, start_c]]
    visited[start_r][start_c] = 1

    while stack:

        r, c = stack.pop()
        if arr[r][c] == 3:
            return 1

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr<0 or nr>=n or nc<0 or nc>=n: continue

            if (arr[nr][nc] == 0 or arr[nr][nc]==3) and not visited[nr][nc]:
                stack.append([nr, nc])
                visited[nr][nc] = 1
    return 0


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                start_r = i
                start_c = j
                break


    print('#{} {}'.format(tc, check(arr, start_r, start_c)))