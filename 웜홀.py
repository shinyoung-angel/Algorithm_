import heapq
import sys
input = sys.stdin.readline

tc = int(input())

def dijkstra(start):
    heap = [(0, start)]
    key = [123456879] * (n+1)
    key[start] = 0

    while heap:
        dist, node = heapq.heappop(heap)
        if key[node] < dist: continue

        for n_dist, n_node in road[node]:
            cost = dist + n_dist
            if cost < key[n_node]:
                key[n_node] = cost
                heapq.heappush(heap, (n_dist, n_node))
    return key

for i in range(tc):
    n, m, w = map(int, input().split())
    road = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        road[a].append((c, b))
        road[b].append((c, a))

    key = dijkstra(1)
    result = 'NO'
    for _ in range(w):
        a, b, c = map(int, input().split())
        if key[a] - c < 0: result = 'YES'

    print(result)



