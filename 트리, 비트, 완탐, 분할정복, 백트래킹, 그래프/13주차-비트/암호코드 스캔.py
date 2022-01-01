

## 오잉


num = {'0001101':0, '0011001':1, '0010011':2, '0111101':3,
       '0100011':4, '0110001':5, '0101111':6, '0111011':7,
       '0110111':8, '0001011':9}

ratio = { '211':0, '221':1, '122':2, '411':3, '132':4,
          '231':5, '114':6, '312':7, '213':8, '112':9}

for tc in range(1, int(input())+1):
    n, m = map(int, input().split())

    ## 16진수 코드가 있는 행 찾아주기
    hexa = []
    for i in range(n):
        row = input().rstrip('0')
        if not row:
            continue
        hexa += [row]

    ## 중복된 행 지워주기
    hexa = set(hexa)

    # 16진수 --> 10진수 --> 2진수
    binary = []
    for item in hexa:
        binary_str = ''
        for i in item:
            binary_str += format(int(i, 16), '04b')

        binary.append(binary_str)


    ##### 암호가 여러 개자너?? 오또카지??

    print(hexa)
    print(binary)
    print(len(binary))


