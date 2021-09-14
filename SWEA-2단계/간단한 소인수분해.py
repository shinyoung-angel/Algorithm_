

for tc in range(1, int(input())+1):
    n = int(input())

    num = {2:0, 3:0, 5:0, 7:0, 11:0}

    while True:

        if n == 1:
            break

        for i in num:
            if n % i == 0:
                num[i] += 1
                n //= i



    print(f'#{tc}', end=' ')
    for i in num.values():
        print(i, end=' ')
    print()