

def bfs(start):
    queue = [start]
    visited[start] = 1

    while queue:
        q = queue.pop(0)
        # print(visited)
        for i in range(1, n+1):
            if arr[q][i] and not visited[i]:
                queue.append(i)
                visited[i] = visited[q] + 1

n = int(input())
x, y = map(int, input().split())
m = int(input())
visited = [0] * (n+1)
arr = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

bfs(x)

if visited[y] == 0:
    print(-1)
else:
    print(visited[y]-1)