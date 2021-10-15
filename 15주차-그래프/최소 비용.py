from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    global extra

    queue = deque([(0, 0)])
    visited[0][0] = 1

    while queue:

        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < n:

                if arr[nr][nc] > arr[r][c]:
                    extra = arr[nr][nc] - arr[r][c]
                else:
                    extra = 0

                if not visited[nr][nc]:
                    visited[nr][nc] = visited[r][c] + 1 + extra
                    queue.append((nr, nc))
                else:
                    if visited[nr][nc] > visited[r][c] + 1 + extra:
                        visited[nr][nc] = visited[r][c] + 1 + extra
                        queue.append((nr, nc))


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    extra = 0

    bfs()
    ans = visited[n-1][n-1] - 1
    print('#{} {}'.format(tc, ans))

###############################################


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():

    queue = [0] * 100000
    front = rear = -1
    rear += 1
    queue[rear] = (0, 0)        ## 행과 열의 좌표를 넣음
    dist[0][0] = 0

    while front != rear:

        front += 1
        r, c = queue[front]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < n:
                extra = arr[nr][nc]-arr[r][c] if arr[nr][nc] > arr[r][c] else 0

                if dist[nr][nc] > dist[r][c] + extra + 1:
                    rear += 1
                    queue[rear] = (nr, nc)
                    dist[nr][nc] = dist[r][c] + extra + 1



for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dist = [[123456789]*n for _ in range(n)]

    bfs()

    print('#{} {}'.format(tc, dist[n-1][n-1]))