import sys
input = sys.stdin.readline

for i in range(int(input())):
    r, e, c = map(int, input().split())

    tmp = (e-c) - r

    if tmp > 0:
        print('advertise')
    elif tmp == 0:
        print('does not matter')
    else:
        print('do not advertise')
