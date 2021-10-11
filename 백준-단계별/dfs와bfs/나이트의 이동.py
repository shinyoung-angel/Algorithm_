from collections import deque

## 8방향의 인덱스 잘보시오~~
dr = [-1, -2, -2, -1, 1, 2, 2, 1]
dc = [-2, -1, 1, 2, -2, -1, 1, 2]

def bfs(r, c):

    queue = deque([(r, c)])
    arr[r][c] = 1

    while queue:

        curr_r, curr_c = queue.popleft()

        for i in range(8):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            if 0 <= nr < n and 0<= nc < n:
                if arr[nr][nc] == 0:
                    queue.append((nr, nc))
                    arr[nr][nc] = arr[curr_r][curr_c] + 1


for tc in range(int(input())):
    n = int(input())
    now_x, now_y = map(int, input().split())
    move_x, move_y = map(int, input().split())
    arr = [[0]*n for _ in range(n)]

    bfs(now_x, now_y)

    ans = arr[move_x][move_y]

    print(ans-1)