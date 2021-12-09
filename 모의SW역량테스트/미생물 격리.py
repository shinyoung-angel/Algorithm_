
def move():
    ## 원래의 방향
    dir = [(0,0), (-1, 0), (1, 0), (0, -1), (0, 1)]
    ## dir의 반대 방향
    reverse_dir = [0, 2, 1, 4, 3]
    # 방문 체크
    check = {}

    ## 군집의 갯수만큼 반복
    for th in range(k):
        group = arr[th]
        r, c, cnt, d = group

        ## 미생물이 없다면 패스
        if cnt == 0: continue

        ## 군집에 새로운 위치를 할당
        nr = r + dir[d][0]
        nc = c + dir[d][1]
        group[0], group[1] = nr, nc

        ## 약품 처리가 된 곳이라면 미생물의 수를 반으로 줄이고, 방향을 반대 방향으로 변경
        if nr == 0 or nr == n-1 or nc == 0 or nc == n-1:
            group[2] //= 2
            group[3] = reverse_dir[d]

        ## 방문한 적이 없다면 방문 쳌
        if (nr, nc) not in check:
            check[(nr,nc)] = (th, cnt)
            continue

        ## 방문한 적이 있다면 이미 담겨 있는 값을 가져오기
        next_th, next_cnt = check[(nr, nc)]
        ## 현재의 미생물 수가 더 많다면
        ## 현재 미생물에 이미 위치에 담겨있는 미생물 수를 더하고
        ## 이전에 담겨 있던 미생물 수를 0으로 초기화
        if cnt > next_cnt:
            group[2] += arr[next_th][2]
            # group[2] += next_cnt   이거는 틀림!!!!! 왜?? --- 같은 위치에 모인 값 중 최대값을 뜻하는 것이니 틀림
            check[(nr, nc)] = (th, cnt)         ## 최대값 갱신
            arr[next_th][2] = 0                 ## 미생물 수가 합쳐졌으니 얘는 초기화
        else:
            arr[next_th][2] += cnt              ## 이미 담겨있는 값이 더 크다면 거기에다 현재 미생물 수를 더해줌
            group[2] = 0                        ## 더해주고 나서 현재 군집의 미생물 수를 0으로 초기화


for tc in range(1, int(input())+1):
    n, m, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(k)]

    ## 주어진 시간만큼 for문을 돌기
    for _ in range(m):
        move()

    result = 0
    for i in range(k):
        result += arr[i][2]

    print('#{} {}'.format(tc, result))
