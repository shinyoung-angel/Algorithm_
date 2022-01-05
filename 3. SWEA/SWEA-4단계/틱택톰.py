

### 행, 열, 대각선 총 10줄을 문자열로 변경하여 각 요소를 count

## o, x, t를 카운트해주는 함수
def check(word):
    cnt_x, cnt_o, cnt_t = 0, 0, 0
    for j in word:
        if j == 'X': cnt_x += 1
        elif j == 'O': cnt_o += 1
        elif j == 'T': cnt_t += 1
    if (cnt_t==1 and cnt_x==3) or cnt_x==4:
        return 'X won'
    elif (cnt_t==1 and cnt_o==3) or cnt_o==4:
        return 'O won'
    return 'Draw'


for tc in range(1, int(input())+1):
    ## 인풋 받을 때 주의!! 공백이 한 줄씩 있음
    if tc == 1:
        arr = [list(input().strip()) for _ in range(4)]
    else:
        arr = [list(input().strip()) for _ in range(5)]
        arr.pop(0)

    board = []                  ## 여기다가 문자열 담아줌
    winner = ''
    for i in range(4):
        tmp_r = ''
        tmp_c = ''
        for j in range(4):
            tmp_r += arr[i][j]  ## 행
            tmp_c += arr[j][i]  ## 열
        board.append(tmp_r)
        board.append(tmp_c)
    board.append(''.join([arr[0][0], arr[1][1], arr[2][2], arr[3][3]])) # 왼쪽 대각선
    board.append(''.join([arr[0][3], arr[1][2], arr[2][1], arr[3][0]])) # 오른쪽 대각선

    for i in range(10):                 ## 총 10줄을 검사해줌
        winner = check(board[i])
        if winner != 'Draw':            ## 승자가 있으면 break
            break

    if winner == 'Draw':                ## 승자가 없을 때
        flag = 0
        for i in range(4):
            for j in range(4):
                if arr[i][j] == '.':    ## 게임이 끝나지 않았을 때
                    winner = 'Game has not completed'
                    flag = 1
                    break
            if flag == 1:
                break
    print('#{} {}'.format(tc, winner))