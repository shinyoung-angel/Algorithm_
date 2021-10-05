# 우 하 좌 상 (시계방향)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
#
T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]

    d = 0  # 방향
    r = 0  # 행좌표
    c = 0  # 열좌표
    num = 1  # 내까 찍을 숫자

    while num <= N * N:
        arr[r][c] = num
        num += 1

        # 다음 칸을 결정을 해야한다.
        nr = r + dr[d]
        nc = c + dc[d]
        # 유효한 좌표인지 검사하자....
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            # 무적권 간다.
            r, c = nr, nc
        else:
            d = (d + 1) % 4
            r += dr[d]
            c += dc[d]

    print("#{}".format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()
#
#################################################################################

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [[0] * N for _ in range(N)]

    r = 0  # 행의 위치
    c = -1  # 열의 위치
    d = 1  # 증감
    K = N  # 이동할 거리
    num = 1  # 넣을 값

    while True:
        # 수평이동
        for i in range(K):
            c += d
            arr[r][c] = num
            num += 1

        # 수평 -> 수직
        K -= 1
        if K == 0: break

        # 수직이동
        for i in range(K):
            r += d
            arr[r][c] = num
            num += 1

        # 수직 -> 수평
        d *= -1

    print("#{}".format(tc))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()