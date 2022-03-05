import sys
input = sys.stdin.readline

n = int(input())
# arr = [list(input().split()) for _ in range(n)]

s = set()

for i in range(n):
    tmp = input().split()

    if tmp[0] == 'add':
        s.add(int(tmp[1]))
    elif tmp[0] == 'remove':
        s.discard(int(tmp[1]))
    elif tmp[0] == 'check':
        if int(tmp[1]) in s:
            print(1)
        else:
            print(0)
    elif tmp[0] == 'toggle':
        if int(tmp[1]) in s:
            s.discard(int(tmp[1]))
        else:
            s.add(int(tmp[1]))
    elif tmp[0] == 'all':
        s = set(i for i in range(1, 21))

    else:
        s = set()