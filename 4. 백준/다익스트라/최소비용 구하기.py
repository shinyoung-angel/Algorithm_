import heapq
import sys
input = sys.stdin.readline


## 다익스트라 알고리즘의 정석
n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append((c, b))

start_node, end_node = map(int, input().split())

def dijkstra(start):
    key = [123456789] * (n+1)
    key[start] = 0
    h = [(0, start)]

    while h:
        dist, node = heapq.heappop(h)

        if key[node] < dist: continue

        for n_dist, n_node in arr[node]:
            cost = dist + n_dist
            if cost < key[n_node]:
                key[n_node] = cost
                heapq.heappush(h, (cost, n_node))

    return key


print(dijkstra(start_node)[end_node])

