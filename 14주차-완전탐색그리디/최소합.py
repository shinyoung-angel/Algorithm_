


# 우하
dr = [0, 1]
dc = [1, 0]

def dfs(r, c, total):
    global min_value


    if r == n-1 and c == n-1:
        total += arr[r][c]
        if total < min_value:
            min_value = total
            return

    if total > min_value:
        return

    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
            visited[nr][nc] = 1
            dfs(nr, nc, total + arr[nr][nc])
            visited[nr][nc] = 0


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]

    min_value = 123456789

    dfs(0, 0, 0)
    print('#{} {}'.format(tc, min_value))
