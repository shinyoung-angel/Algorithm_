숫자 배열

for i in range(1, int(input()) + 1):
    test_num = int(input())
    data = list(map(int, input().split()))
    ans = ''
    for j in range(len(data) - 1, 0, -1):
        for k in range(j):
            if data[k] > data[k + 1]:
                data[k], data[k + 1] = data[k + 1], data[k]

            ans = " ".join(map(str, data))

    print(f'#{i} {ans}')

