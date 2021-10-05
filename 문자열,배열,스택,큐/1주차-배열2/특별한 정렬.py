def bubble(data):
    for i in range(len(data)-1, 0, -1):
        for k in range(i):
            if data[k] > data[k+1]:
                data[k], data[k+1] = data[k+1], data[k]
    return data

for tc in range(1, int(input())+1):
    N = int(input())
    TC = list(map(int, input().split()))

    bubble(TC)
    ans = []

    for i in range(5):
        ans.append(TC[-1-i])
        ans.append(TC[i])


    print('#{}'.format(tc), end= " ")
    for k in ans:
        print('{}'.format(k), end = " ")
    print()


