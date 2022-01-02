import sys
input = sys.stdin.readline


for tc in range(int(input())):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    idx = list(range(len(arr)))
    idx[m] = 'tmp'
    cnt = 0

    while True:

        if arr[0] == max(arr):
            cnt += 1

            if idx[0] == 'tmp':
                print(cnt)
                break
            arr.pop(0)
            idx.pop(0)

        else:
            arr.append(arr.pop(0))
            idx.append(idx.pop(0))

