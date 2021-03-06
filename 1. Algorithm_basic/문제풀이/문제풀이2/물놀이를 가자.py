

###################################

from collections import deque

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]

    dist = [[123456789] * m for _ in range(n)]  # 방문췤 겸 거리 췤

    Q = deque()

    # 시작점인 물을 몽땅 담아두기 위해서
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'W':
                Q.append((i, j))
                dist[i][j] = 0

    while Q:

        r, c = Q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= n or nc < 0 or nc >= m: continue
            if arr[nr][nc] == 'L' and dist[nr][nc] == 123456789:
                dist[nr][nc] = dist[r][c] + 1
                Q.append((nr, nc))



    ans = 0

    for i in dist:
        for j in i:
            ans += j

    print('#{} {}'.format(tc, ans))


# ------------------

###################################

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]

    dist = [[123456789] * m for _ in range(n)]  # 방문췤 겸 거리 췤

    ## 만약 deque를 import할 수 없다면
    Q = [0] * (n*m)
    front = -1
    rear = -1

    # 시작점인 물을 몽땅 담아두기 위해서
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'W':
                rear += 1
                Q[rear] = (i, j)
                dist[i][j] = 0

    while front != rear:

        front += 1
        r, c = Q[front]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= n or nc < 0 or nc >= m: continue
            if arr[nr][nc] == 'L' and dist[nr][nc] == 123456789:
                dist[nr][nc] = dist[r][c] + 1

                rear += 1
                Q[rear] = (nr, nc)


    ans = 0

    for i in dist:
        for j in i:
            ans += j

    print('#{} {}'.format(tc, ans))


#####################################################런타임 에러 뜨네~~~~~~~~~~~~~~~~~~~


##########런타임 에러 이유는
##input을 리스트로 받아서 그럼
## 그냥 문자열로 받으니까 멀쩡한디,,,,,,.

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


for tc in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    visited = [[-1]*m for _ in range(n)]

    queue = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'W':
                queue.append((i, j))
                visited[i][j] = 0

    while queue:

        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == 'L' and visited[nr][nc] == -1:
                    queue.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            cnt += visited[i][j]

    print('#{} {}'.format(tc, cnt))
