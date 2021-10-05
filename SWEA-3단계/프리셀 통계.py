T = int(input())
for tc in range(1, T + 1):
    N, pd, pg = map(int, input().split())
    def is_chk():
        if pg == 100 or pg == 0:
            if pg != pd:
                return 0
        if N >= 100:
            return 1
        elif N >= 10 and pd % 10 == 0:
            return 1
        else:
            for i in range(N, 0, -1):
                if (i * pd) % 100 == 0:
                    return 1
        return 0


    if is_chk():
        print('#{} Possible'.format(tc))
    else:
        print('#{} Broken'.format(tc))

#
def check():



for tc in range(1, int(input())+1):
    n, pd, pg = map(int, input().split())

    print('#{} {}'.format(tc, check()))