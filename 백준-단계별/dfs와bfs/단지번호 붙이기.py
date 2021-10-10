
# dr = [1, 0, -1, 0]
# dc = [0, 1, 0, -1]
#
# def bfs(r, c):
#
#     queue = [(r, c)]
#     visited[r][c] = 1
#     cnt = 0
#
#     while queue:
#
#         curr_r, curr_c = queue.pop(0)
#         cnt += 1
#
#         for i in range(4):
#             nr = curr_r + dr[i]
#             nc = curr_c + dc[i]
#
#             if 0 <= nr < n and 0 <= nc < n:
#                 if arr[nr][nc] and not visited[nr][nc]:
#                     visited[nr][nc] = 1
#                     queue.append((nr, nc))
#
#     return cnt
#
#
# n = int(input())
# arr = [list(map(int, input())) for _ in range(n)]
# visited=[[0]*n for _ in range(n)]
# color = 0
# value_list = []
#
# for i in range(n):
#     for j in range(n):
#         if arr[i][j] and not visited[i][j]:
#             value = bfs(i, j)
#             color += 1
#             value_list.append(value)
#
#
# value_list.sort()
# print(color)
# for i in value_list:
#     print(i)


##########################################################################

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c):
    global cnt

    visited[r][c] = 1
    cnt += 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < n and 0 <= nc < n:
            if arr[nr][nc] and not visited[nr][nc]:
                dfs(nr, nc)

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
ans = []

for i in range(n):
    for j in range(n):
        if arr[i][j] and not visited[i][j]:
            cnt = 0
            dfs(i, j)
            ans.append(cnt)

ans.sort()
print(len(ans))
for i in ans:
    print(i)
