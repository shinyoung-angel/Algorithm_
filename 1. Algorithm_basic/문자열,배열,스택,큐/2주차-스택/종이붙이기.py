

def check(n):

    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return check(n-1) + (2*check(n-2))

for tc in range(1, int(input())+1):
    n = int(input())
    num = n // 10

    print('#{} {}'.format(tc, check(num)))

