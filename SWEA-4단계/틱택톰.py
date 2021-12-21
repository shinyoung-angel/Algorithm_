

for tc in range(1, int(input())+1):
    arr = [list(input()) for _ in range(4)]
    print(arr)

###
def get_winner(row):
    x_cnt, o_cnt, t_cnt = 0, 0, 0
    for c in row:
        if c == 'X':
            x_cnt += 1
        elif c == 'O':
            o_cnt += 1
        elif c == 'T':
            t_cnt += 1
    if x_cnt + t_cnt == 4:
        return 'X won'
    elif o_cnt + t_cnt == 4:
        return 'O won'
    return None


T = int(input())
for t in range(1, T + 1):
    if t != 1:
        input()
    board = []
    done = True
    for _ in range(4):
        row = input()
        if '.' in row:
            done = False
        board.append(row)
    for i in range(4):
        vert = []
        for j in range(4):
            vert.append(board[j][i])
        board.append(''.join(vert))
    board.append(''.join([board[0][0], board[1][1], board[2][2], board[3][3]]))
    board.append(''.join([board[3][0], board[2][1], board[1][2], board[0][3]]))
    for i in range(10):
        winner = get_winner(board[i])
        if winner:
            print("#{} {}".format(t, winner))
            break
    if not winner:
        if not done:
            print("#{} Game has not completed".format(t))
        else:
            print("#{} Draw".format(t))