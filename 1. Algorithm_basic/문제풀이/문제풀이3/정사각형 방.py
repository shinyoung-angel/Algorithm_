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

############################################
## 위치와 거리를 한번에 담기

for tc in range(1, int(input())+1):
    n = int(input())
    arr = []

    room_position = [0] * (n*n+1)               # 룸의 위치를 저장
    room_distance = [0] * (n*n+1)               # 해당 번호까지 지나온 방의 개수를 저장

    # 입력받으면서 위치 정보를 저장.
    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(n):
            room_position[tmp[j]] = (i, j)
        arr.append(tmp)

    # 거리 정보를 저장
    for i in range(2, n*n+1):
        for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            nr = room_position[i][0] + dr
            nc = room_position[i][1] + dc


            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == i-1:
                room_distance[i] == room_distance[i-1] + 1
                break

    value = 0
    max_value = 0

    for i in range(1, n*n+1):
        if room_distance[i] > max_value:
            value = i
            max_value = room_distance[i]

    print('#{} {} {}'.format(tc, value-max_value +1, max_value))