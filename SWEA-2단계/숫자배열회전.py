
# 90, 180, 270만큼 도는 함수를 선언
# 함수를 호출하면 세 개의 리스트가 반환됨. 세 아이를 각 a, b, c 라고 이름을 붙였음.
# 그리고 세 리스트의 첫 번째 요소들부터 한 줄로 출력하고 마지막에는 다음 줄로 넘어가게 함.


def rotation(arr):

    arr_90 = [[0]*n for _ in range(n)]
    arr_180 = [[0]*n for _ in range(n)]
    arr_270 = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            arr_90[i][j] = arr[n-1-j][i]
            arr_180[i][j] = arr[n-1-i][n-1-j]
            arr_270[i][j] = arr[j][n-1-i]

    return arr_90, arr_180, arr_270

for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    a, b, c = rotation(arr)

    print(f'#{tc}')

    for i in range(n):
        for j in range(n):
            print(a[i][j], end='')
        print(end=' ')
        for j in range(n):
            print(b[i][j], end ='')
        print(end=' ')
        for j in range(n):
            print(c[i][j], end ='')
        # 마지막 아이 후에는 줄넘김 해야함!!!
        print()

