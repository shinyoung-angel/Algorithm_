

## idx: index, n: 숫자 갯수
def selection(idx, n):

    if idx == n:
        print(arr)

    else:

        for i in range(idx+1, n):
            if arr[idx] > arr[i]:
                arr[idx], arr[i] = arr[i], arr[idx]
        selection(idx+1, n)


arr = [6, 4, 1, 3, 5, 2]
## 시작 인덱스는 0이라 0을 넣어 줌
selection(0, len(arr))

