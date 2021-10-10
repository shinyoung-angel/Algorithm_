## run time error로 모듈을 썼다.
### bfs로 최단 경로를 확인하는 것이지만
#### 시작점이 여러 개인 것을 고려하기 !!! 그럴 땐 리스트에 한번에 담아주기
##### 생각보다 유용한 조건표현식

import sys
from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

def bfs():

    while queue:
        curr_r, curr_c = queue.popleft()

        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            if nr < 0 or nr >= n or nc < 0 or nc >= m: continue
            if arr[nr][nc] == 0:
                queue.append((nr, nc))
                arr[nr][nc] = arr[curr_r][curr_c] + 1


m, n = map(int, sys.stdin.readline().split())
arr = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            queue.append((i, j))

bfs()


ans = 1
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            ans = 0
            break
    if ans == 0:
        break

if ans == 0:
    print(-1)
else:
    ans = max(map(max, arr)) - 1
    print(ans)

###################################

ans = True
result = max(map(max, arr)) - 1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            ans = False
            break
    if not ans:
        break

print(result if ans else -1)