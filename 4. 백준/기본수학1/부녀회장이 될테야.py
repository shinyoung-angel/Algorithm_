# 사람들의 수를 담을 arr 생성. 모든 1호에는 1명만 사니까 기본 값을 1로 설정함
# 0층에는 1,2,3,,, 요렇게니까 0층에 사람 수 넣어 줌.
# 그리고 k층의 n호까지 사람 수를 채워줄 것인데 해당 호수의 왼쪽 집과 아래 층의 같은 호수 사람 수를 더해줌.

for _ in range(int(input())):
    k = int(input())
    n = int(input())

    arr = [[1]*n for _ in range(k+1)]

    for i in range(1, n):
        arr[0][i] = i+1


    # 층 수가 0층 부터라 k+1까지
    for i in range(1, k+1):
        for j in range(1, n):
            arr[i][j] = arr[i][j-1] + arr[i-1][j]

    print(arr[k][n-1])

