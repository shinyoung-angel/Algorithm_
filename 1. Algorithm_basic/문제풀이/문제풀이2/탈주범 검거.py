

## 우화좌상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

pipe = [
    [0, 0, 0, 0],
    [1, 1, 1, 1], #상하좌우
    [0, 1, 0, 1], # 상하
    [1, 0, 1, 0], # 좌우
    [1, 0, 0, 1], # 상우
    [1, 1, 0, 0], # 하우
    [0, 1, 1, 0], # 하좌
    [0, 0, 1, 1] #상좌
]

for tc in range(1, int(input())+1):
    n, m, r, c, l = map(int, input().split())
    tunnel = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)] # 시간췤 겸 방문 췤

    Q = [(r, c)]
    visited[r][c] = 1

    ans = 0

    while Q:
        r, c = Q.pop(0)
        ans += 1

        if visited[r][c] >= l: continue

        # 사방향 탐색
        for d in range(4):
            curr_p = tunnel[r][c]
            # 현재 바라보는 방향으로 길이 없다면
            if pipe[curr_p][d] == 0: continue

            nr = r + dr[d]
            nc = c + dc[d]

            # 다음 좌표가 맵을 벗어났다면
            if nr < 0 or nr >= n or nc < 0 or nc >= m: continue


            nd = (d+2) % 4
            np = tunnel[nr][nc]

            # 방문을 했거나, 다음 좌표의 파이프가 현재 좌표와 연결되지 않는다면!!!
            if visited[nr][nc] or pipe[np][nd] == 0: continue

            visited[nr][nc] = visited[r][c] + 1
            Q.append((nr, nc))


    print('#{} {}'.format(tc, ans))


## dfs 가넝

#######################

dr = [0, 1, 0, -1]  # 구미 2반 윤수현님
dc = [1, 0, -1, 0]  # 서울 5반 김종우님.

pipe = [
    [],
    [0, 1, 2, 3],
    [1, 3],
    [0, 2],
    [0, 3],
    [0, 1],
    [1, 2],
    [2, 3]
]


def DFS(r, c, time):
    visited[r][c] = time
    if time == L: return

    for i in pipe[tunnel[r][c]]:
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < M and\
                tunnel[nr][nc] and\
                ((i + 2) % 4 in pipe[tunnel[nr][nc]]) and\
                visited[nr][nc] > time:
            DFS(nr, nc, time + 1)


T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    # 지도 정보
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[987654321] * M for _ in range(N)]  # 방문 쳌

    DFS(R, C, 1)

    ans = 0

    for i in range(N):
        for j in range(M):
            if visited[i][j] != 987654321:
                ans += 1

    print("#{} {}".format(tc, ans))


