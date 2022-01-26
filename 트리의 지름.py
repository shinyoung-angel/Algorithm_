


import sys
input = sys.stdin.readline

# v = int(input())
#
#
# ## 주어진 거리를 할당하기
# arr = [[0]*(v+1) for _ in range(v+1)]
# for _ in range(v):
#     tmp = list(map(int, input().split()))
#     start = tmp[0]
#     for i in range(1, len(tmp), 2):
#         node = tmp[i]
#         if node == -1:
#             break
#         else:
#             dist = tmp[i + 1]
#             arr[start][node] = dist
#             arr[node][start] = dist
#








########## dfs로 풀면 메모리 초과~~~~~~~~~~~~~~

from collections import deque
v = int(input())


## 주어진 거리를 할당하기
arr = [[0]*(v+1) for _ in range(v+1)]
for _ in range(v):
    tmp = list(map(int, input().split()))
    start = tmp[0]
    for i in range(1, len(tmp), 2):
        node = tmp[i]
        if node == -1:
            break
        else:
            dist = tmp[i + 1]
            arr[start][node] = dist
            arr[node][start] = dist

def dfs(start):
    stack = deque([start])
    visited[start] = 1

    while stack:

        t = stack.pop()
        for j in range(1, v+1):
            if arr[t][j] and not visited[j]:
                arr[start][j] = arr[start][t] + arr[t][j]
                stack.append(j)
                visited[j] = 1

for i in range(1, v+1):
    visited = [0] * (v+1)
    dfs(i)

result = max(map(max, arr))
print(result)