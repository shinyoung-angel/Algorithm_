

num = {'0001101':0, '0011001':1, '0010011':2, '0111101':3,
       '0100011':4, '0110001':5, '0101111':6, '0111011':7,
       '0110111':8, '0001011':9}


for tc in range(1, int(input())+1):
    n, m = map(int, input().strip().split())
    arr = [input() for _ in range(n)]

    code = ''
    flag = 0
    for i in range(n):
        for j in range(m-1, -1, -1):
            if arr[i][j] == '1':
                code += arr[i][j-55:j+1]
                flag = 1
                break
        if flag == 1:
            break

    check = []
    start, end = 0, 7
    for i in range(8):
        check.append(num[code[start:end]])
        start += 7
        end += 7


    check_sum = 0

    for i in range(8):
        if i % 2 == 0:
            check_sum += 3*check[i]
        else:
            check_sum += check[i]

    if check_sum % 10 == 0:
        print('#{} {}'.format(tc, sum(check)))
    else:
        print('#{} {}'.format(tc, 0))








# ---------------------

num = {'0001101':0, '0011001':1, '0010011':2, '0111101':3,
       '0100011':4, '0110001':5, '0101111':6, '0111011':7,
       '0110111':8, '0001011':9}


for tc in range(1, int(input())+1):
    n, m = map(int, input().strip().split())
    arr = [input() for _ in range(n)]

    code = ''
    flag = 0
    for i in range(n):
        for j in range(m-1, -1, -1):
            if arr[i][j] == '1':
                code += arr[i][j-55:j+1]
                flag = 1
                break
        if flag == 1:
            break

    check = []
    start, end = 0, 7
    for i in range(8):
        check.append(num[code[start:end]])
        start += 7
        end += 7


    if ((check[0]+check[2]+check[4]+check[6])*3 + check[1]+check[3]+check[5] + check[7]) % 10 == 0:
        print('#{} {}'.format(tc, sum(check)))
    else:
        print('#{} {}'.format(tc, 0))