dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
### 1은 아직 벽이 있는 상태
### 0은 벽을 허물었다.

def bfs():
    queue = [(0, 0, 1)]

    while queue:
        r, c, wall = queue.pop(0)

        if r == n-1 and c == m-1:
            return v[r][c][wall]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == 0 and v[nr][nc][wall] == 0:       # 벽을 허물었든 안 허물었든 이동 가능
                    v[nr][nc][wall] = v[r][c][wall] + 1
                    queue.append((nr, nc, wall))
                elif arr[nr][nc] == 1 and wall == 1:                # 벽이 있으며 허물 수 있음
                    v[nr][nc][0] = v[r][c][1] + 1
                    queue.append((nr, nc, 0))
    return -1

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
v = [[[0]*2 for _ in range(m)] for _ in range(n)]
v[0][0][1] = 1      # 벽이 있다

print(bfs())

