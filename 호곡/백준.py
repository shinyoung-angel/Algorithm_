

def dfs(start):
    pass
def bfs(start):

    queue = [start]
    visited_bfs[start] = 1
    while queue:

        hey = queue.pop(0)
        print(hey, end=' ')

        for i in range(1, n+1):
            if arr[hey][i] and not visited[i]:
                queue.append(i)
                visited_bfs[i] = 1


n, m, v = map(int, input().split())

## 인접 행렬
arr = [[0]*(n+1) for _ in range(n+1)]
visited_dfs = [0] * (n+1)
visited_bfs = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1
dfs(v)
bfs(v)

