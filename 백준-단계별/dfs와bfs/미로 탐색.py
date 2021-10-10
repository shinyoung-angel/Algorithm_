

####### 갹 이거 bfs자나~~~~~~~
####### 최단 경로를 찾는 문제


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def bfs(r, c):

    queue = [(r, c)]
    visited[r][c] = 1

    while queue:

        curr_r, curr_c = queue.pop(0)

        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] and not visited[nr][nc]:
                    queue.append((nr, nc))
                    visited[nr][nc] = visited[curr_r][curr_c] + 1



n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

bfs(0, 0)
ans = visited[n-1][m-1]

print(ans)