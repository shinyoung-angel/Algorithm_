import heapq
import sys
input = sys.stdin.readline

def dijkstra(node, key):
    heap = []
    heapq.heappush(heap, (0,node))
    key[node] = 0

    while heap:
        w, n = heapq.heappop(heap)

        if key[n] < w: continue

        for weight, idx in adj[n]:
            next_weight = weight + w
            if key[idx] > next_weight:
                key[idx] = next_weight
                heapq.heappush(heap, (next_weight, idx))


n, e = map(int, input().split())
adj = [[] for _ in range(n+1)]

for i in range(e):
    st, ed, w = map(int, input().split())
    adj[st].append((w, ed))
    adj[ed].append(((w, st)))

v1, v2 = map(int, input().split())

key_start = [123456789] * (n+1)
key_v1 = [123456789] * (n+1)
key_v2 = [123456789] * (n+1)

dijkstra(1, key_start)
dijkstra(v1, key_v1)
dijkstra(v2, key_v2)

## 1번에서 출발해서 v1을 들린 후, v1에서 최단 경로로 v2를 갔다가, v2에서 최단 경로로 종점 가긔
method1 = key_start[v1] + key_v1[v2] + key_v2[n]
method2 = key_start[v2] + key_v2[v1] + key_v1[n]
result = min(method1, method2)

print(result if result < 123456789 else -1)