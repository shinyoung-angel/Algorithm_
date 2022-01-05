for tc in range(1, 11):
    N = input()
    arr = list(map(int, input().split()))
    i = 1

    while True:

        if arr[0] - i <= 0:
            arr.append(0)
            arr.pop(0)
            break

        else:
            arr.append(arr[0]-i)
            arr.pop(0)
            i += 1

        if i > 5:
            i = 1

    arr = ' '.join(map(str, arr))
    print('#{} {}'.format(tc, arr))

