

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))

    for i in range(M):
        num.append(num.pop(0))

    print('#{} {}'.format(tc, num[0]))