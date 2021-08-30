# 영감탱 가만안둬


# 이거 실ㅋ 패   77개 맞음 나머지는 왜 틀린지 잘 모루겠따
def check():

    # 가로
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 'o':
                cnt += 1
            else:
                if cnt == 5:
                    return 'YES'
                cnt = 0
        if cnt == 5:
            return 'YES'

    #세로
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 'o':
                cnt += 1
            else:
                if cnt == 5:
                    return 'YES'
                cnt = 0
        if cnt == 5:
            return 'YES'

    # 대각선 1
    cnt = 0
    for i in range(N):
        if arr[i][i] == 'o':
            cnt += 1
        else:
            if cnt == 5:
                return 'YES'
            cnt = 0
    if cnt == 5:
        return 'YES'


    # 대각선 2
    cnt = 0
    for i in range(N):
        if arr[i][N-1-i] == 'o':
            cnt += 1
        else:
            if cnt == 5:
                return 'YES'
            cnt = 0
    if cnt == 5:
        return 'YES'

    return 'NO'


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    print('#{} {}'.format(tc, check()))


# -------------------------------------------------
def check ():

    for i in range(N):

        for j in range(N-4):
            cnt = 0
            for k in range(5):
                if arr[i][j+k] == 'o':
                    cnt += 1
            if cnt == 5:
                return 'YES'

            cnt = 0
            for h in range(5):
                if arr[j+h][i] == 'o':
                    cnt += 1
            if cnt == 5:
                return 'YES'


    for k in range(N-5+1):
        for m in range(N-5+1):
            cnt = 0
            for z in range(5):
                if arr[k+z][m+z] == 'o':
                    cnt += 1
            if cnt == 5:
                return 'YES'

            cnt = 0
            for z in range(5):
                if arr[k+z][N-1-m-z] == 'o':
                    cnt += 1
            if cnt == 5:
                return 'YES'
    return 'NO'



for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    print('#{} {}'.format(tc, check()))

# ---------------

def check_five(r, c):
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    for t in range(8):
        nr, nc = r, c
        # 시작좌표를 r,c 로 세팅. 2차원 배열을 열우선으로 하나씩 탐색하면서 매번 새로운 x, y 좌표를
        # check_five 함수에 받아온 뒤 시작 좌표로 세팅한다.
        cnt = 0
        while cnt < 5 and 0 <= nr < n and 0 <= nc < n:
            if MAP[nr][nc] == 'o':
                # 한 방향을 지정 했으면 그 방항으로 쭉 더하면서 cnt가 5가 될때까지 while문으로 반복해준다.

                cnt += 1
                nr += dr[t]
                nc += dc[t]
            else:
                break
        if cnt == 5:
            return 1

    return 0


T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    MAP = [input() for _ in range(n)]

    flag = 0
    for r in range(n):
        for c in range(n):
            if MAP[r][c] == 'o':
                result = check_five(r, c)
                # (r,c) 에서 8 방향 검사

                if result == 1:
                    # 검사 후 1로 리턴을 받았으면 flag = 1

                    flag = 1
                    break

    if flag == 1:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')

#--------------------------------------

def omok():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'o':
                for d in range(4):
                    ni = i + di[d]
                    nj = j + dj[d]
                    cnt = 1
                    while 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 'o':
                        cnt += 1
                        ni = ni + di[d]
                        nj = nj + dj[d]
                        if cnt >= 5: return "YES"
    return "NO"


di = [0, 1, 1, 1]
dj = [1, 0, 1, -1]
for tc in range(1, 1 + int(input())):
    N = int(input())
    board = [list(input()) for _ in range(N)]
    print("#{} {}".format(tc, omok()))



