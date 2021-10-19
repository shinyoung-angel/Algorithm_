
import heapq

def dijkstra():

    heap = []
    heapq.heappush(heap, (0, start))
    key[start] = 0

    while heap:

        w, node = heapq.heappop(heap)

        if key[node] < w: continue

        for weight, idx in adj[node]:
            next_weight = weight + w
            if key[idx] > next_weight:
                key[idx] = next_weight
                heapq.heappush(heap, (next_weight, idx))


v, e = map(int, input().split())
start = int(input())
adj = [[] for _ in range(v+1)]
key = [123456789] * (v+1)

for i in range(e):
    st, ed, w = map(int, input().split())
    adj[st].append((w, ed))

dijkstra()

for i in range(1, v+1):
    if key[i] == 123456789:
        print('INF')
    else:
        print(key[i])