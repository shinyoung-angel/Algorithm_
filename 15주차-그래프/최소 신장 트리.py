


for tc in range(1, int(input())+1):
    n, e = map(int, input().split())
    arr = [[123456789]*(n+1) for _ in range(n+1)]
    key = [123456789] * (n+1)
    visited = [0] * (n+1)
    key[0] = 0

    for i in range(e):
        st, ed, w = map(int, input().split())
        arr[st][ed] = w
        arr[ed][st] = w

    ## 최소 인덱스 값 찾기 // 값 갱신
    ## 맨 마지막 정점은 돌지 못함.
    for i in range(n):

        min_idx = -1
        min_value = 123456789

        for i in range(n+1):
            if not visited[i] and key[i] < min_value:
                min_idx = i
                min_value = key[i]

        ### 최소의 정점을 찾고 방문 췤
        visited[min_idx] = 1

        for i in range(n+1):
            if not visited[i] and arr[min_idx][i] < key[i]:
                key[i] = arr[min_idx][i]


    print('#{} {}'.format(tc, sum(key)))
