


for tc in range(1, int(input())+1):
    arr = list(map(int, input().split()))
    stop = arr[0]
    charge = arr[1:]
    count = [0] * (stop+1)

    count[0] = -1

    for i in range(stop-1):
        for j in range(1, charge[i]+1):
            count[i+j] = min(count[i]+1, count[i+j])

    print('#{} {}'.format(tc, count[stop-1]))

