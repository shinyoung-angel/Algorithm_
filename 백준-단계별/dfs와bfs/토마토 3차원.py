import sys
from collections import deque
input = sys.stdin.readline

##### 2차원으로 생각하지 말고 3차원으로 생각하기~~~~~~~~~~~~~~~~~~
## 3차원 input은 어떻게 받을 지 잘 생각하라

dr = [1, -1, 0, 0, 0, 0]
dc = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]

def bfs():

    while queue:
        height, r, c = queue.popleft()

        for i in range(6):
            nr = r + dr[i]
            nc = c + dc[i]
            nh = height + dh[i]

            if 0<= nr < n and 0 <= nc < m and 0 <= nh < h:
                if arr[nh][nr][nc] == 0:
                    arr[nh][nr][nc] = arr[height][r][c] + 1
                    queue.append((nh, nr, nc))


m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for depth in range(h)]       ##3차원 리스트 받기

queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:                       ## 익은 토마토 인덱스 받기
                queue.append((i, j, k))

bfs()

flag = -1
result = -1

for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0:                       ## 익지 않은 토마토 -> flag=0
                flag = 0
            else:
                result = max(result, arr[i][j][k])      ## 3차원에서 최대값 찾기

if flag == 0:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result-1)