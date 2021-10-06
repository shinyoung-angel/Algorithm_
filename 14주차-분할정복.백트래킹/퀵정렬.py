

def partition(A, l, r):
    ## 왼쪽 아이가 피봇
    p = A[l]
    i, j = l,r

    while i <= j:

        while i <= j and A[i] <= p:
            i += 1

        while i <= j and A[j] >= p:
            j -= 1

        if i < j:
            A[i], A[j] = A[j], A[i]

    A[l], A[j] = A[j], A[l]
    return j


def quick_sort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        quick_sort(A, l, s-1)
        quick_sort(A, s+1, r)

arr = [6, 2, 8, 1, 7, 5, 3, 9, 4]
quick_sort(arr, 0, len(arr)-1)
print(arr)