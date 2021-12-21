
for tc in range(1, int(input())+1):
    arr = [list(input()) for _ in range(4)]

    winner = 'Draw'
    for i in range(4):
        row_x, row_o, row_t = 0, 0, 0
        col_x, col_o, col_t = 0, 0, 0
        for j in range(4):
            now_r, now_c = arr[i][j], arr[j][i]
            if now_r == 'X': row_x += 1
            elif now_r == 'O': row_o += 1
            elif now_r == 'T': row_t += 1

            if now_c == 'X': col_x += 1
            elif now_c == 'O': col_o += 1
            elif now_c == 'T': col_t += 1
        if (row_t==1 and row_x==3) or (row_t==1 and row_o==3) or (row_t)