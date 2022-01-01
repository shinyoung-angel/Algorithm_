
def quick_sort(arr, left, right):

    p = arr[left]                                   # 젤 왼쪽 요소를 피벗으로 설정
    i, j = left, right                              # 왼쪽, 오른쪽 인덱스를 i, j로 설정 (포인터)

    while i <= j:                                   # i가 j보다 커지면 탈출

        while i <= j and arr[i] <= p:               # 피벗보다 큰 수가 나오면 멈춰
            i += 1

        while i <= j and arr[j] >= p:               # 피벗보다 작은 수가 나오면 멈춰
            j -= 1

        if i < j:                                   # 오른쪽, 왼쪽 둘 다 멈추고 인덱스를 아직 침범하지 않았다면 스왑
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]           # while문을 탈출했다면 피벗과 i, j가 교차한 지점을 스왑
    return j                                        # 피벗의 인덱스를 반환



def divide(arr, left, right):                           #최소한의 단위로 분할

    if left < right:
        pivot = quick_sort(arr, left, right)            # 퀵 소트
        divide(arr, left, pivot-1)
        divide(arr, pivot+1, right)


for tc in range(1, int(input())+1):
    n = int(input())
    arr = list(map(int, input().split()))
    divide(arr, 0, len(arr)-1)

    print('#{} {}'.format(tc, arr[n//2]))



# -----------------------------------------------

# 가장 오른쪽 아이를 기준으로 정렬하는 로무토는 시간이 오래 걸림

def lomuto(arr, l, r):
    pivot = arr[r]              # 가장 오른쪽 구역
    i = l-1                     # 경계구역

    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

