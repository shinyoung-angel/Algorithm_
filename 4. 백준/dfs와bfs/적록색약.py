import copy
import sys
from collections import deque
input = sys.stdin.readline
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

n = int(input())

arr = []
arr_unnormal = []

for i in range(n):
    tmp = list(input())
    arr.append(copy.deepcopy(tmp))
    for j in range(n):
        if tmp[j] == 'G':
            tmp[j] = 'R'
    arr_unnormal.append(tmp)

noraml = 0
unnormal = 0

visited_noraml = [[0]*n for _ in range(n)]
visited_unnoraml = [[0]*n for _ in range(n)]

def bfs(visit, map, x, y):
    visit[x][y] = 1
    queue = deque([(x, y)])
    color = map[x][y]

    while queue:
        curr_r, curr_c = queue.popleft()

        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]

            if 0<= nr < n and 0 <= nc < n:
                if not visit[nr][nc] and map[nr][nc] == color:
                    queue.append((nr, nc))
                    visit[nr][nc] = 1

    return 1


### 요 for문과 밑의 for문을 함께 돌리면 틀림!!!!!!!!!!!!
### for문을 분리시키면 ㅇㅋ
for i in range(n):
    for j in range(n):
        if not visited_noraml[i][j]:
            noraml += bfs(visited_noraml, arr, i, j)

for i in range(n):
    for j in range(n):
        if not visited_unnoraml[i][j]:
            unnormal += bfs(visited_unnoraml, arr_unnormal, i, j)

print(noraml, unnormal)
