
# 재귀로 하니까 runtime error가 뜬다
### 재귀로 하되 sys.setrecursionlimit(10**8) 요렇게 달아주기
## 숫자가 커진다면 재귀 ㄴㄴ

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def dfs(r, c):

    stack = [(r, c)]
    visited[r][c] = 1

    while stack:

        curr_r, curr_c = stack.pop()

        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    stack.append((nr, nc))


for tc in range(int(input())):
    m, n, k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())
        arr[x][y] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] and not visited[i][j]:
                dfs(i, j)
                cnt += 1

    print(cnt)


####################################

import sys
sys.setrecursionlimit(10**8)

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def dfs(r, c):

    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < n and 0 <= nc < m:
            if arr[nr][nc] and not visited[nr][nc]:
                dfs(nr, nc)


for tc in range(int(input())):
    m, n, k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]

    for _ in range(k):
        y, x = map(int, input().split())
        arr[x][y] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] and not visited[i][j]:
                dfs(i, j)
                cnt += 1

    print(cnt)