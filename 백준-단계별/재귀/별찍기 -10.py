
### 진촤 넘 어렵당


def star(i):
    global arr

    idx = []
    for i in range(n):
        if (i//3 ** cnt_) % 3 == 1:
            idx.append(i)

    for i in idx:
        for j in idx:
            arr[i][j] = ' '

n = int(input())
v = n
cnt = 0

while v!=1:
    v /= 3
    cnt += 1

arr = [['*']*n for _ in range(n)]
for cnt_ in range(cnt):
    star(cnt_)

for i in range(n):
    for j in range(n):
        print(arr[i][j], end='')
    print()


# -----------------


def star(n):
    unit_size = int(n / 3)
    if n == 3:
        fig = []
        fig.append('*'*n)
        fig.append('*'+' '*unit_size+'*')
        fig.append('*'*n)
        return fig
    else:
        fig1 = star(unit_size)
        fig = [i*3 for i in fig1]
        fig += [i+' '*unit_size+i for i in fig1]
        fig += [i*3 for i in fig1]
        return fig


n = int(input())
fig = star(n)
for i in fig:
    print(i)


# --------------------

N = int(input())


def starlist(n):
    if n == 1:
        return ['*']
    else:
        slist = []
        before = n // 3

        for i in starlist(before):
            slist.append(i * 3)
        for i in starlist(before):
            slist.append(i + ' ' * before + i)
        for i in starlist(before):
            slist.append(i * 3)

        return slist


print('\n'.join(starlist(N)))


# -------------------------

def star(n, x, y):

    ## break 조건은 n이 3이 되었을 때 == 최소한의 단위
    if n == 3:
        arr[x][y:y+3] = ['*', '*', '*']
        arr[x+1][y:y+3] = ['*', ' ', '*']
        arr[x+2][y:y+3] = ['*', '*', '*']
        return

    ## 3의 배수로 나누며 별 채우기를 반복할 것임
    next_size = n // 3
    ## 항상 삼등분 해서 별 채우기를 진행하니까 3 x 3 for문이 필요함.
    for dx in range(3):
        for dy in range(3):
            ### 중간 네모를 비워줘야 함 조건은 dx, dy 모두 1일 때
            if dx != 1 or dy != 1:
                ### 작은 네모들로 재귀 호출
                star(next_size, x + dx * next_size, y + dy * next_size)


N = int(input())
arr = [[' ']*N for _ in range(N)]
star(N, 0, 0)

for i in arr:
    print(''.join(i))


#---------------------

def remover(n=0):
    if 3 ** n >= test_case:
        return
    for ti in range(3 ** n, test_case, 3 ** (n + 1)):
        for tj in range(3 ** n, test_case, 3 ** (n + 1)):
            star[ti][tj] = ' '
            if n:
                for ti_2 in range(ti, ti + 3 ** n):
                    for tj_2 in range(tj, tj + 3 ** n):
                        star[ti_2][tj_2] = ' '

    remover(n + 1)


test_case = int(input().strip())
star = [['*'] * test_case for _ in range(test_case)]
remover()

for si in range(test_case):
    for sj in range(test_case):
        print(star[si][sj], end='')
    print()
