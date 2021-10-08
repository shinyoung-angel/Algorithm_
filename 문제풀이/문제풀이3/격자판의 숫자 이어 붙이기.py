
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def check(r, c, line):
    global ans

    if len(line) == 7:
        ans.add(line)
        return

    for i in range(6):
        nr = r + dr[i % 4]
        nc = c + dc[i % 4]

        if nr < 0 or nr >= 4 or nc < 0 or nc >= 4: continue
        check(nr, nc, line + arr[nr][nc])



for tc in range(1, int(input())+1):
    arr = [list(input().split()) for _ in range(4)]
    ans = set()


    for i in range(4):
        for j in range(4):
            check(i, j, arr[i][j])


    print('#{} {}'.format(tc, len(ans)))




# ---------------------------------------------

##
def check(r, c, line):

    if len(line) == 7:

        if line not in ans:
            ans.append(line)
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >=4 or nc <0 or nc >=4: continue
        check(nr, nc, line+arr[nr][nc])


for tc in range(1, int(input())+1):
    n = 4
    arr = [input().split() for _ in range(4)]
    ans = []


    for i in range(n):
        for j in range(n):
            check(i, j, arr[i][j])


    print('#{} {}'.format(tc, len(ans)))


###################################################################


def dfs2(r, c, num, idx):          # 좌표, 만들고있는 숫자, 어디자리까지 만들었는지
    if idx == 7:
        ans.add(num)
        return
    else:

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < n:
                dfs2(nr, nc, num*10 + arr[nr][nc], idx+1)



for tc in range(1, int(input())+1):
    n = 4
    arr = [list(map(int, input().split())) for _ in range(4)]
    ans = set()


    for i in range(n):
        for j in range(n):
            dfs2(i, j, arr[i][j], 1)


    print('#{} {}'.format(tc, len(ans)))