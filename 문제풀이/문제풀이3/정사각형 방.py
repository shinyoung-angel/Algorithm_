dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * (n*n+1)

    for i in range(n):
        for j in range(n):
            tmp = arr[i][j]

            for k in range(4):
                nr = i + dr[k]
                nc = j + dc[k]

                if 0 <= nr < n and 0 <= nc < n:
                    if arr[nr][nc] == arr[i][j] + 1:
                        visited[tmp] = 1
                        break
    cnt = 0
    value = 0
    max_value = 0

########## visited 리스트에서 뒤에서부터 값을 갱신해주면 가장 작은 값을 가질 수 있다~~~~~~~~~~~
    for i in range(len(visited)-1, -1, -1):
        if visited[i] == 1:                 # 1이 나오면 cnt 카운팅
            cnt += 1
        elif cnt:                           # cnt가 값은 있지만 지금은 0인 경우 갱신을 하거나 하지 않음.
            if cnt >= max_value:
                max_value = cnt
                value = i + 1
            cnt = 0
        else:                               # 없어도 되지만 넣어줌.
            continue

    print('#{} {} {}'.format(tc, value, max_value+1))

