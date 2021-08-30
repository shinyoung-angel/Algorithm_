# min-max

for i in range(1, int(input())+1):
    N = int(input())
    data = list(map(int, input().split()))
    ans = ''
    for k in range(N-1, 0, -1):
        for j in range(k):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

        ans = data[-1] - data[0]

    print('#{} {}'.format(i, ans))


