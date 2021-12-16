

n, k = map(int, input().split())
arr = list(map(int, input().split()))
box = [0] * 2 * n

box[0] = 1
cnt = 0

while True:

    for i in range(1, 2*n):
        if box[i-1] == 1:
            if box[i] == 0 and arr[i] >= 1:
                box[i] = 1
                box[i - 1] = 0
                arr[i-1] -= 1
            if arr[i-1] == 0:
                cnt += 1

    if box[0] == 0 and arr[0] >= 1:
        box[0] = 1

    if cnt == k:
        break

print(cnt)

