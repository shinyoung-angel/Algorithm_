
def win(player):

    for i in range(10):

        ## triplet
        if player[i] >= 3:
            return 1
        ## run
        elif player[i] >= 1 and player[i+1] >=1 and player[i+2] >= 1:
            return 1

    return 0



for tc in range(1, int(input())+1):
    num = list(map(int, input().split()))
    check_1 = [0] * 12
    check_2 = [0] * 12

    ## check에다가 숫자 넣어주기 홀수 인덱스 -> 선수2/ 짝수 인덱스 -> 선수1
    ## 카드가 들어올 때마다 함수로 췤 해준다
    for i in range(12):
        if i % 2 == 0:
            check_1[num[i]] += 1
            if win(check_1):
                winner = 1
                break
        else:
            check_2[num[i]] += 1
            if win(check_2):
                winner = 2
                break

    else:
        winner = 0


    print('#{} {}'.format(tc, winner))



