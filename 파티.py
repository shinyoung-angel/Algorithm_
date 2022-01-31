import sys, heapq
input = sys.stdin.readline

people, roads, destination = map(int, input().split())
arr = [[] for _ in range(people+1)]

for _ in range(roads):
    a, b, c = map(int, input().split())
    arr[a].append((c, b))

def dijkstra(start):
    q = []
    key = [1000000000] * (people+1)
    key[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, node = heapq.heappop(q)

        ## 이미 작은 값이 있다면 통과
        if key[node] < dist: continue

        for n_dist, n_node in arr[node]:
            cost = dist + n_dist
            if cost < key[n_node]:
                key[n_node] = cost
                heapq.heappush(q, (cost, n_node))


    return key

destination_to_town = dijkstra(destination)
town_to_destination = [0] * (people+1)

for person in range(1, people+1):
    if person != destination:
        tmp = dijkstra(person)
        town_to_destination[person] += tmp[destination]

ans = 0
for i in range(1, people+1):
    ans = max(ans, destination_to_town[i] + town_to_destination[i])

print(destination_to_town)
print(town_to_destination)
print(ans)

# result = 0
# for i in range(1, people+1):
#     go = dijkstra(i)
#     back = dijkstra(destination)
#     result = max(result, go[destination]+back[i])
#
# print(result)
