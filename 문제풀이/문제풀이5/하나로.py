


for tc in range(1, int(input())+1):
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    e = float(input())
    key = [123456789] * n
    visited = [0] * n
    key[0] = 0

    ## 최단 거리 저장하기
    arr = [[123456789]*n for _ in range(n)]
    for i in range(n-1):
        a_x = x[i]
        a_y = y[i]
        for j in range(n):
            b_x = x[j]
            b_y = y[j]
            arr[i][j] = arr[j][i] = ((a_x-b_x)**2 + (a_y-b_y)**2)**0.5


    for i in range(n-1):

        min_idx = -1
        min_value = 123456789

        for i in range(n):
            if not visited[i] and key[i] < min_value:
                min_idx = i
                min_value = key[i]

        visited[min_idx] = 1

        for i in range(n):
            if not visited[i] and key[i] > arr[min_idx][i]:
                key[i] = arr[min_idx][i]

    ans = 0
    for i in key:
        ans += i ** 2
    result = ans * e

    print('#{} {}'.format(tc, round(result)))