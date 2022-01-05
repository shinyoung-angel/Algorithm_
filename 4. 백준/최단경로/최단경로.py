
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())
arr = [[123456789]*(v+1) for _ in range(v+1)]
key = [123456789] * (v+1)
visited = [0] * (v+1)
key[start] = 0

for i in range(e):
    st, ed, w = map(int, input().split())
    arr[st][ed] = w

## 마지막 정점은 정해진 값이니 돌 필요가 x
for _ in range(v):

    min_idx = 0
    min_value = 123456789

    #### 최소값을 가진 인덱스 찾기
    for i in range(v+1):
        if key[i] < min_value and not visited[i]:
            min_idx = i
            min_value = key[i]
    ## 최소 정점을 찾았다면 방문 췤
    visited[min_idx] = 1

    ### 인접한 값들을 갱신
    for i in range(v+1):
        if not visited[i] and key[i] > key[min_idx] + arr[min_idx][i]:
            key[i] = key[min_idx] + arr[min_idx][i]

for i in range(1, v+1):
    if key[i] == 123456789:
        print('INF')
    else:
        print(key[i])



########################

import heapq

def dijkstra():

    heap = []
    heapq.heappush(heap, (0, start))
    key[start] = 0

    while heap:

        w, node = heapq.heappop(heap)

        if key[node] < w:
            continue

        for weight, idx in adj[node]:
            next_weight = w + weight
            if next_weight < key[idx]:
                key[idx] = next_weight
                heapq.heappush(heap, (next_weight, idx))

v, e = map(int, input().split())
start = int(input())
adj = [[] for _ in range(v+1)]
key = [123456789] * (v+1)


for i in range(e):
    st, ed, w = map(int, input().split())
    adj[st].append((w, ed))                 ## 방향이 왜 있노??????
    # adj[ed].append((w, st))

dijkstra()

for i in range(1, v+1):
    if key[i] == 123456789:
        print('INF')
    else:
        print(key[i])