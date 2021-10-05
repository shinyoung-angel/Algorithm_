
for i in range(1, int(input())+1):
    N, M = map(int, input().split())
    TC = list(map(int, input().split()))
    max_value = 0
    min_value = 123456


    for k in range(N-M+1):
        temp = 0
        for j in range(M):
            temp += TC[k+j]
        if temp > max_value:
            max_value = temp
        if temp < min_value:
            min_value = temp

    print('#{} {}'.format(i, max_value - min_value))



