




# --------------------------

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    ## 최소값으로 값을 더해주는 리스트 생성
    arr_count = [[0]*n for _ in range(n)]

    # 첫 번째 행과 열에 숫자를 미리 넣어주기
    for i in range(n):

        # 제일 첫번째 숫자 담기
        if i == 0:
            arr_count[0][i] += arr[0][i]

        else:
            arr_count[0][i] += arr_count[0][i-1] + arr[0][i]
            arr_count[i][0] += arr_count[i-1][0] + arr[i][0]


    for i in range(1, n):
        for j in range(1, n):
            arr_count[i][j] = min(arr_count[i][j-1]+arr[i][j], arr_count[i-1][j]+arr[i][j])

    print('#{} {}'.format(tc, arr_count[n-1][n-1]))