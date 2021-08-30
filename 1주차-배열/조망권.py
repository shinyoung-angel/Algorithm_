
for k in range(1, 11):
    N = int(input())
    data = list(map(int, input().split()))
    cnt = 0

    for j in range(2, N-2):
        max_value = -1

        if data[j] > data[j-1] and data[j] > data[j-2] and data[j] > data[j+1] and data[j] > data[j+2]:
            for i in (data[j-1], data[j-2], data[j+1] ,data[j+2]):
                if i > max_value:
                    max_value = i

            cnt += data[j] - max_value

    print('#{} {}'.format(k, cnt))