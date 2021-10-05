

for tc in range(1, int(input())+1):
    N = int(input())
    stop_list = [list(map(int, input().split())) for _ in range(N)]
    stop = [0] * 5001

    for i in range(N):
        for k in range(stop_list[i][0], stop_list[i][1] + 1):
            stop[k] += 1


    P = int(input())

    print('#{}'.format(tc), end = ' ')
    for i in range(P):
        print(stop[int(input())], end = ' ')
    print()

    # 위에처럼 해도 되고 아래처럼 해도되고
    # print('#{}'.format(tc), end=' ')
    # for i in range(P):
    #     C = int(input())
    #     print(stop[C], end=' ')
    # print()

# --------------------------------

for tc in range(1, int(input())+1):
    N = int(input())
    stop = [0] * 5001

    for i in range(N):
        A, B = list(map(int, input().split()))

        for k in range(A, B + 1):
            stop[k] += 1


    P = int(input())

    print('#{}'.format(tc), end=' ')
    for i in range(P):
        C = int(input())
        print(stop[C], end=' ')
    print()



