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
    tmp = list(map(int, input().split()))
    arr.append(tmp)
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