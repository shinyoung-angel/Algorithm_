

## 구구단1 -------------------------
for tc in range(1, int(input())+1):
    n = int(input())

    ## 가능한 경우의 수를 모두 딕셔너리에 넣어 놓고 여기서 숫자를 찾기
    num = {}

    for i in range(1, 10):
        for j in range(1, 10):
            if not num.get(i*j):
                num[i*j] = 1

    if num.get(n):
        print('#{} Yes'.format(tc))
    else:
        print('#{} No'.format(tc))
#------------------------------------------------

for tc in range(1, int(input())+1):
    n = int(input())
    result = 'No'

    for i in range(1, 10):
        if n % i == 0 and n // i < 10:
            result = 'Yes'
            break

    print('#{} {}'.format(tc, result))
# -----------------

for tc in range(1, int(input())+1):
    n = int(input())
    result = 'No'
    num = n
    cnt = 0
    ans = 1



    for i in range(9, 0, -1):
        for j in range(9, 0, -1):
            if n == i * j:
                cnt += 2
                break
        if cnt == 2:
            break

    if cnt == 2:
        result = 'Yes'

    print('#{} {}'.format(tc, result))