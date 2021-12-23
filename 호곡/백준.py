
for tc in range(1, int(input())+1):

    if tc == 1:
        arr = [list(input().strip()) for _ in range(4)]
    else:
        arr = [list(input().strip()) for _ in range(5)]
        arr.pop(0)

    winner = 'Draw'
    for i in range(4):
        if winner != 'Draw':
            break
        row_x, row_o, row_t = 0, 0, 0
        col_x, col_o, col_t = 0, 0, 0
        for j in range(4):
            now_r = arr[i][j]
            now_c = arr[j][i]
            if now_r == 'X': row_x += 1
            elif now_r == 'O': row_o += 1
            elif now_r == 'T': row_t += 1

            if now_c == 'X': col_x += 1
            elif now_c == 'O': col_o += 1
            elif now_c == 'T': col_t += 1
        if (row_t==1 and row_x==3)  or row_x == 4:
            winner = 'X won'
            break
        elif (row_t==1 and row_o==3) or row_o == 4:
            winner = 'O won'
            break

    left_x, left_o, left_t = 0, 0, 0
    right_x, right_o, right_t = 0, 0, 0
    if winner == 'Draw':
        for i in range(4):
            if winner != 'Draw':
                break
            for j in range(4):
                tmp = arr[i][j]
                if i == j:
                    if tmp == 'X': left_x += 1
                    elif tmp == 'O': left_o += 1
                    elif tmp == 'T': left_t += 1
                elif i + j == 3:
                    if tmp == 'X': right_x += 1
                    elif tmp == 'O': right_o += 1
                    elif tmp == 'T': right_t += 1
            if (left_t == 1 and left_x == 3) or left_x == 4 or right_x == 4 or (right_t==1 and right_x==3):
                winner = 'X won'
                break
            elif (left_t==1 and left_o==3) or left_o==4 or right_o==4 or (right_t==1 and right_o==3):
                winner = 'O won'
                break


    if winner == 'Draw':
        flag = 0
        for i in range(4):
            for j in range(4):
                if arr[i][j] == '.':
                    winner = 'Game has not completed'
                    flag = 1
                    break
            if flag == 1:
                break

    print('#{} {}'.format(tc, winner))
