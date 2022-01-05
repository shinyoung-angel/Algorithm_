import sys
input = sys.stdin.readline

def merge(left, right):

    pa, pb, pc = 0, 0, 0
    na, nb = len(left), len(right)
    result = [0] * (na+nb)

    while pa < na and pb < nb:
        if left[pa] <= right[pb]:
            result[pc] = left[pa]
            pc += 1
            pa += 1
        else:
            result[pc] = right[pb]
            pc += 1
            pb += 1
    while pa < na:
        result[pc] = left[pa]
        pc += 1
        pa += 1

    while pb < nb:
        result[pc] = right[pb]
        pc += 1
        pb += 1

    return result

def divide(num):

    if len(num) <= 1:
        return num

    mid = len(num) // 2
    left = divide(num[:mid])
    right = divide(num[mid:])
    return merge(left, right)


n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

for i in divide(arr):
    print(i)