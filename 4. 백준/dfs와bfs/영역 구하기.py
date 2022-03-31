import sys
input = sys.stdin.readline

from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

m, n, k = map(int, input().split())
arr = [[0]*n for _ in range(m)]

for _ in range(k):
    a, b, c, d = map(int, input().split())
    for i in range(b, d):
        for j in range(a, c):
            arr[i][j] = 1

result = []
visited = [[0]*n for _ in range(m)]
def dfs(x, y):

    queue = deque()
    queue.append([x, y])
    cnt = 0
    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < m and 0 <= nc < n and arr[nr][nc] == 0:
                if not visited[nr][nc]:
                    visited[nr][nc] = 1
                    queue.append([nr, nc])
                    cnt += 1

    result.append(cnt)

region = 0
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0 and not visited[i][j]:
            region += 1
            dfs(i, j)

result.sort()
print(region)
for i in result:
    if i == 0:
        print(1, end=' ')
    else:
        print(i, end=' ')