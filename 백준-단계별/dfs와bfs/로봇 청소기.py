

dir = [(-1,0), (0,1), (1,0), (0,-1)]

def clean(r,c,d):
    global cnt
    nd =d
    for i in range(4):
        nd = (nd+3) % 4
        nr = r + dir[nd][0]
        nc = c + dir[nd][1]

        if 0 <= nr < n and 0 <= nc < m:
            if arr[nr][nc] == 0:
                arr[nr][nc] = 2
                cnt += 1
                clean(nr, nc, nd)
                return
    nd = (nd+2) % 4
    nr = r + dir[nd][0]
    nc = c + dir[nd][1]

    if arr[nr][nc] == 1:
        return
    else:
        clean(nr, nc, nd)



n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cnt = 1
arr[r][c] = 2
clean(r,c,d)
print(cnt)