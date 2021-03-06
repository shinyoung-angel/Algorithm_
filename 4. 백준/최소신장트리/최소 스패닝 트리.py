## 크루스칼

import sys
input = sys.stdin.readline


def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)

v, e = map(int, input().split())
adj = [list(map(int, input().split())) for _ in range(e)]
p = list(range(v+1))
adj.sort(key=lambda x: x[2])

cnt = 0
ans = 0
idx = 0

while cnt < v-1:

    n1 = adj[idx][0]
    n2 = adj[idx][1]

    if find_set(n1) != find_set(n2):
        union(n1, n2)
        cnt += 1
        ans += adj[idx][2]
    idx += 1

print(ans)

# for n1, n2, w in adj:
#     if find_set(n1) != find_set(n2):
#         cnt += 1
#         ans += w
#         union(n1, n2)
#         if cnt == v-1:
#             break
#
# print(ans)


####################################### 이건 왜 안되지 ??????????????????????????????????????메모리초과


inf = sys.maxsize


def prim():

    visited = [0] * (v+1)
    key[1] = 0

    for _ in range(v-1):

        min_idx = -1
        min_value = inf

        for i in range(1, v+1):
            if not visited[i] and key[i] < min_value:
                min_idx = i
                min_value = key[i]

        visited[min_idx] = 1

        for i in range(1, v+1):
            if not visited[i] and key[i] > arr[min_idx][i]:
                key[i] = arr[min_idx][i]


v, e = map(int, input().split())
arr = [[inf]*(v+1) for _ in range(v+1)]
key = [inf] * (v+1)

for i in range(e):
    a, b, c = map(int, input().split())
    arr[a][b] = c
    arr[b][a] = c

prim()

ans = sum(key[1:])
print(ans)
