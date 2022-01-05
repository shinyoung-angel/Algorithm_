


for tc in range(1, int(input())+1):
    d, l, n = map(int, input().split())

    cnt = 0
    damage = 0

    for i in range(n):
        damage += d*(1+ (i*l*0.01))

    print('#{} {}'.format(tc, int(damage)))