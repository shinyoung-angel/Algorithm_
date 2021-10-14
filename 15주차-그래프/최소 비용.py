from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def bfs():
    global extra

    queue = deque([(0, 0)])
    visited[0][0] = 1

    while queue:

        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < n:

                if arr[nr][nc] > arr[r][c]:
                    extra = arr[nr][nc] - arr[r][c]
                else:
                    extra = 0

                if not visited[nr][nc]:
                    visited[nr][nc] = visited[r][c] + 1 + extra
                    queue.append((nr, nc))
                else:
                    if visited[nr][nc] > visited[r][c] + 1 + extra:
                        visited[nr][nc] = visited[r][c] + 1 + extra
                        queue.append((nr, nc))


for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    extra = 0

    bfs()
    ans = visited[n-1][n-1] - 1
    print('#{} {}'.format(tc, ans))

###############################################

#### runtime error

# def dfs(r, c, cnt, extra):
#     global ans
#
#     visited[r][c] = 1
#
#     if cnt + extra > ans:
#         return
#
#     if r == n-1 and c == n-1:
#         ans = cnt + extra
#         return ans
#
#     for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#
#             if 0 <= nr < n and 0 <= nc < n:
#                 if visited[nr][nc] == 0:
#                     if arr[nr][nc] > arr[r][c]:
#                         dfs(nr, nc, cnt+1, extra + arr[nr][nc] - arr[r][c])
#                         visited[nr][nc] = 0
#                     else:
#                         dfs(nr, nc, cnt+1, extra)
#                         visited[nr][nc] = 0
#
#
#
# for tc in range(1, int(input())+1):
#     n = int(input())
#     arr = [list(map(int, input().split())) for _ in range(n)]
#     visited = [[0]*n for _ in range(n)]
#     ans = 123456
#
#     dfs(0, 0, 0, 0)
#
#     print('#{} {}'.format(tc, ans))
