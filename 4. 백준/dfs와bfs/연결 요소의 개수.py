import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0]*(n+1) for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    arr[a][b] = 1
    arr[b][a] = 1

def dfs(node):
    q = deque([node])
    visited[node] = 1

    while q:
        t = q.popleft()
        for i in range(1, n+1):
            if arr[t][i] and not visited[i]:
                q.append(i)
                visited[i] = 1

ans = 0
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        ans += 1

print(ans)


# import sys
# input = sys.stdin.readline

# sys.setrecursionlimit(10000)  ----------> 이거이거 없으면 런타임 에러 남~~

# n, m = map(int, input().split())
# arr = [[0]*(n+1) for _ in range(n+1)]
# visited = [0] * (n+1)
#
# for _ in range(m):
#     a, b = map(int, input().split())
#     arr[a][b] = 1
#     arr[b][a] = 1
#
# def dfs(node):
#
#     visited[node] = 1
#     for i in range(1, n+1):
#         if arr[node][i] and not visited[i]:
#             dfs(i)
#
# ans = 0
# for i in range(1, n+1):
#     if not visited[i]:
#         dfs(i)
#         ans += 1
#
# print(ans)