
import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):
    global n

    key = [123456789] * (n+1)
    heap = []
    heapq.heappush(heap, (0, start))
    key[start] = 0

    while heap:
        w, node = heapq.heappop(heap)

        # if key[n] < w: continue

        for weight, idx in adj[node]:
            next_weight = weight + w
            if key[idx] > next_weight:
                key[idx] = next_weight
                heapq.heappush(heap, (next_weight, idx))
    return key

for tc in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    adj = [[] for _ in range(n+1)]

    for i in range(m):
        st, ed, w = map(int, input().split())
        adj[st].append((w, ed))
        adj[ed].append((w, st))

    s_start = dijkstra(s)
    g_start = dijkstra(g)
    h_start = dijkstra(h)

    path1 = s_start[g] + g_start[h]
    path2 = s_start[h] + h_start[g]

    ans_list = []
    for i in range(t):
        destination = int(input())
        a = path1 + h_start[destination]
        b = path2 + g_start[destination]
        c = s_start[destination]
        if a == c or b == c:
            ans_list.append(destination)

    ans_list.sort()

    print(*ans_list)





