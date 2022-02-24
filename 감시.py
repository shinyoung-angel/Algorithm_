
## 방향
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

n, m = map(int, input().split())
arr = []
cctv_cnt = 0
cctv_position = []

for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
    for j in range(m):
        if tmp[j] != 0 and tmp[j] != 6:
            cctv_cnt += 1
            cctv_position.append([i, j])

for axis in range(cctv_cnt):
    tmp = arr[cctv_position[0]][cctv_position[1]]

    for dir in range(4):

        if tmp == 1:
            pass


