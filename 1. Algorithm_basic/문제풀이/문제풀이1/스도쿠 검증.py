
def check():
    for i in range(9):
        # 해당 원소를 사용했나 안했나 체크
        row = [0] * 10
        col = [0] * 10


        for j in range(9):
            #행
            num_row = TC[i][j]
            #열 검사
            num_col = TC[j][i]

            # 이미 사용한 숫자라면 멈춰
            if row[num_row]: return 0
            if col[num_col]: return 0

            row[num_row] = 1
            col[num_col] = 1

            if i % 3 == 0 and j % 3 == 0:
                square = [0]*10
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        num = TC[r][c]
                        # 중복된 숫자가 나온다면 그만
                        if square[num]: return 0
                        square[num] = 1
    return 1

for tc in range(1, int(input())+1):
    TC = [list(map(int, input().split())) for _ in range(9)]

    print('#{} {}'.format(tc, check()))

# ---------------------

def sudoku(n_list):
    check = [1] * 9
    for r in range(9):
        count_r = [0] * 9
        count_c = [0] * 9
        for c in range(9):
            count_r[n_list[r][c] - 1] += 1
            count_c[n_list[c][r] - 1] += 1
        if count_r != check or count_c != check:
            return 0

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            count_box = [0] * 9
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    count_box[n_list[x][y] - 1] += 1
            if count_box != check:
                return 0

    return 1


T = int(input())
for tc in range(1, T + 1):
    n_list = [list(map(int, input().split())) for _ in range(9)]
    print('#{} {}'.format(tc, sudoku(n_list)))