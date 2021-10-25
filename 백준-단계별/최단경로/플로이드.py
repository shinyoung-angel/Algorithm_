import sys
import heapq
input = sys.stdin.readline



def check(x):
    key = [123456789] * (n+1)
    key[x] = 0
    heap = []
    heapq.heappush(heap, (0, x))

    while heap:
        w, n = heapq.heappop(heap)

        for weight, node in adj[n]:
            next_weight = weight

n = int(input())
m = int(input())
adj = [[] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((c, b))

for i in range(1, n+1):
    check(i)
