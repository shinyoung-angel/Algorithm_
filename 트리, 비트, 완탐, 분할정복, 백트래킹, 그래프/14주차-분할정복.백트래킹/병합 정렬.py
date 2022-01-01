

def merge(left, right):
    global cnt

    na, nb = len(left), len(right)          # 배열 왼쪽, 오른쪽 길이
    result = [0] * (na+nb)                  # 최종 정렬된 리스트
    pa, pb, pc = 0, 0, 0                    # 왼쪽, 오른쪽, 최종으로 정렬 될 리스트의 포인터(인덱스)

    if left[-1] > right[-1]:                # 왼쪽 젤 오른쪽 아이가 오른쪽 젤 오른쪽 아이보다 크면 카운트
        cnt += 1

    while pa < na and pb < nb:              # 왼쪽, 오른쪽 번갈아가며 result에 값을 채워줌.
        if left[pa] <= right[pb]:           # 왼쪽 요소가 오른쪽 요소보다 작다면 result에 추가
            result[pc] = left[pa]
            pc += 1
            pa += 1
        else:
            result[pc] = right[pb]
            pc += 1
            pb += 1

    while pa < na:                          # 왼쪽에 남아 있는 요소들을 마저 담아줌.
        result[pc] = left[pa]
        pc += 1
        pa += 1

    while pb < nb:                          # 오른쪽에 있는 요소들을 마저 담아줌.
        result[pc] = right[pb]
        pc += 1
        pb += 1

    return result


def divide(arr):                            # 분할해주는 함수

    if len(arr) <= 1:
        return arr
    mid = len(arr) //2
    left = divide(arr[:mid])
    right = divide(arr[mid:])
    return merge(left, right)


for tc in range(1, int(input())+1):
    cnt = 0
    n = int(input())
    arr = list(map(int, input().split()))

    print('#{} {} {}'.format(tc, divide(arr)[n//2], cnt))

