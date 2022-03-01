import  copy
import sys
input = sys.stdin.readline

## 방향
## 동 서 남 북
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
direction = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[0, 2], [2, 1], [1, 3], [3, 0]],
             [[3, 0, 2], [1, 3, 0], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]]

n, m = map(int, input().split())
arr = []
cctv_cnt = 0
queue = []
ans = 123456789999999999999
def watch(x, y, dir, tmp):
    for d in dir:
        nx = x
        ny = y
        while True:
            nx += dr[d]
            ny += dc[d]
            if 0 <= nx < n and 0 <= ny < m and tmp[nx][ny] != 6:
                if tmp[nx][ny] == 0:
                    tmp[nx][ny] = '#'
            else:
                break

def dfs(arr, cnt):
    global ans

    tmp = copy.deepcopy(arr)
    if cnt == cctv_cnt:
        c = 0
        for i in tmp:
            c += i.count(0)
        ans = min(ans, c)
        return
    x, y, cctv = queue[cnt]
    for dir in direction[cctv]:
        watch(x, y, dir, tmp)
        dfs(tmp, cnt+1)
        tmp = copy.deepcopy(arr)

for i in range(n):
    tmp = list(map(int, input().split()))
    arr.append(tmp)
    for j in range(m):
        if tmp[j] != 0 and tmp[j] != 6:
            cctv_cnt += 1
            queue.append([i, j, tmp[j]])

dfs(arr, 0)
print(ans)

