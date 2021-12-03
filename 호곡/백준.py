
dh = [0, 0, 0, 0, -1, 1]
dr = [-1, 1, 0, 0, 0, 0]
dc = [0, 0, -1, 1, 0, 0]

def bfs(hh, xx, yy):
    queue = [(hh, xx, yy)]

    while queue:
        h, x, y = queue.pop(0)

        for i in range(6):
            nh = h + dh[i]
            nr = x + dr[i]
            nc = y + dc[i]

            if 0 <= nh < h and 0 <= nr < n and 0 <= nc < m:
                if tomato[nh][nr][nc] == 0:
                    tomato[nh][nr][nc] = 1
                    queue.append((nh, nr, nc))

m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
cnt = 0
print(tomato)
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                cnt += 1
                bfs(i,j,k)

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                cnt = -1
                break

print(cnt)
print(tomato)