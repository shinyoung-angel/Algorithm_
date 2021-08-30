

def check (a, b):

    if len(a) != len(b):
        return 'DIFF'

    ans = 0
    for i in range(len(a)):

        if a[i] in no_hole and b[i] in no_hole:
            ans += 1
        elif a[i] in yes_hole and b[i] in yes_hole:
            ans += 1
        elif a[i] == 'B' and b[i] == 'B':
            ans += 1

    if ans == len(a):
        return 'SAME'
    return 'DIFF'


for tc in range(1, int(input())+1):
    a, b = input().split()

    no_hole = 'CEFGHIJKLMNSTUVWXYZ'
    yes_hole = 'ADOPQR'

    print('#{} {}'.format(tc, check(a,b)))

