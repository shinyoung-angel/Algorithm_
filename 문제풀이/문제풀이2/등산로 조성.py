


dfs 사용
방문처리 & 재귀

방문했다가 방문췍 풀면서 나옴 우하좌상 순


## 우 하 좌 상
dr =[-1, 1, 0, 0]
dc = [0, 0, -1, 1]

## 1. 현재 위치를 들고다니지 않을 때
## r,c 좌표/ road 등산로 길이/ skill 공사 유무
def work(r,c,road,skill):
    global ans
    if road > ans:
        ans = road

    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
            # a. 현 위치보다 낮은 곳으로 이동할 때
            if mountain[r][c] > mountain[nr][nc]:
                work(nr, nc, road+1, skill)
            # b. 현 위치보다 높거나 같은 곳으로 이동할 때
            elif skill and mountain[r][c] > mountain[nr][nc] - k:
                tmp = mountain[nr][nc] ## 기록
                mountain[nr][nc] = mountain[r][c] - 1
                work(nr, nc, road+1, 0)  ## 공사해썽
                mountain[nr][nc] = tmp ## 원상복구

    visited[r][c] = 0


## 2. 현재 위치를 들고다니자우
def work2(r, c, h, road, skill): ## h는 높이
    global ans
    if road > ans: ans = road
    visited[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr < 0 or nr >= n or nc <0 or nc >= n or visited[nr][nc]: continue
        if h > mountain[nr][nc]:
            work2(nr, nc, mountain[nr][nc], road+1, skill)
        elif skill and h > mountain[nr][nc] - k:
            work2(nr, nc, mountain[r][c]-1, road+1, 0)



for tc in range(1, int(input())+1):
    n, k = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(n)]
    max_h = 0

    # 최고 높이의 봉우리를 찾는 과정 --> 값을 다 받고 찾기
    for i in range(n):
        for j in range(n):
            if max_h < mountain[i][j]:
                max_h = mountain[i][j]


    # ## 값을 받음과 동시에 최대값을 찾기
    # mountain = []
    # max_h = 0
    # for i in range(n):
    #     tmp = list(map(int, input().split()))
    #     for j in tmp:
    #         if max_h < j:
    #             max_h = j
    #     mountain.append(tmp)

    visited = [[]*n for _ in range(n)]
    ans = 0

    for i in range(n):
        for j in range(n):
            if mountain[i][j] == max_h:
                work(i, j, 1, 1) # 좌표, 길, 공사
                # work2(i, j, max_h, 1, 1)


    print('#{} {}'.format(tc, ans))





