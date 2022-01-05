from collections import deque
import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs(x,y):

    queue = deque([(x,y)])
    visited[x][y] = 0

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < n:
                if visited[nr][nc] == 123:
                    queue.append((nr,nc))
                    visited[nr][nc] = 0


n = int(input())
arr = []
num_list = set()
for _ in range(n):
    ## 2차원 리스트 만들기
    tmp = list(map(int, input().split()))
    arr.append(tmp)
    ## 각 요소들을 중복 없이 num_list애 담기
    for i in tmp:
        num_list.add(i)


## 높이에 따라 방문 쳌하고 dfs돌기
result = set()
for num in num_list:
    visited = [[123]*n for _ in range(n)]
    ## 높이가 num이하이면 방문쳌 0으로 변경
    for i in range(n):
        for j in range(n):
            if arr[i][j] <= num:
                visited[i][j] = 0
    cnt = 0
    ## 해당 영역을 bfs 탐색
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 123:
                bfs(i,j)
                cnt += 1

    ## 영역의 갯수들을 result에 담아두기
    result.add(cnt)

##### 모든 지역의 높이가 같은 경우는 답이 0이 아닌 1이다.
answer = max(result)
if answer == 0:
    print(1)
else:
    print(answer)


########################################################

sys.setrecursionlimit(100000)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(x, y):

    visited[x][y] = 1

    for i in range(4):
        nr = x + dr[i]
        nc = y + dc[i]

        if 0 <= nr < n and 0 <= nc < n:
            if arr[nr][nc] > num and not visited[nr][nc]:
                dfs(nr, nc)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
num_range = max(map(max, arr))                              ## 2차원 리스트에서 max값 찾는 방법 (각 행에서 최대값을 찾은 후 그 값들 중의 최대값을 찾기)
result = 0

for num in range(num_range):
    visited = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > num and visited[i][j] == 0:      ## 해당 높이 이상인 요소들을 dfs탐색하기
                dfs(i, j)
                cnt += 1
    result = max(result, cnt)

print(result)
