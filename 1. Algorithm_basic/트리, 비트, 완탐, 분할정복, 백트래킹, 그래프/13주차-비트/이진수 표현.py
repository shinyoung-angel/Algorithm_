
def check():

    if len(binary) < n:
        return 'OFF'
    else:
        cnt = 0
        for i in range(-n, 0, 1):
            if binary[i] == '1':
                cnt += 1

        if cnt == n:
            return 'ON'

    return 'OFF'

for tc in range(1,int(input())+1):
    n, m = map(int, input().split())

    # 앞에 0b를 땠음
    binary = bin(m)[2:]


    print('#{} {}'.format(tc, check()))



