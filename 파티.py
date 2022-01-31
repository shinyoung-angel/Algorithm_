import sys, heapq
input = sys.stdin.readline

people, roads, destination = map(int, input().split())
arr = [[] for _ in range(people+1)]

### 다익스트라 알고리즘을 이해하고 푸니 꽤나 쉽다.

for _ in range(roads):
    a, b, c = map(int, input().split())
    arr[a].append((c, b))

def dijkstra(start):
    q = []
    key = [1000000000] * (people+1)         ## key에 101이라고 뒀을 때 오답 --> 1000000으로 변경
    key[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, node = heapq.heappop(q)

        ## 이미 작은 값이 있다면 통과
        if key[node] < dist: continue

        ## 인접 거리, 인접한 노드
        for n_dist, n_node in arr[node]:
            cost = dist + n_dist    ## 새 거리 = 인접 거리 + 지금 노드의 거리
            if cost < key[n_node]:  ## 새 거리가 원래의 거리보다 작다면
                key[n_node] = cost  ## 갱신
                heapq.heappush(q, (cost, n_node))


    return key

destination_to_town = dijkstra(destination)     ## 목적지 --> town
town_to_destination = [0] * (people+1)          ## town --> 목적지

for person in range(1, people+1):
    if person != destination:
        tmp = dijkstra(person)
        town_to_destination[person] += tmp[destination]

ans = 0
for i in range(1, people+1):
    ans = max(ans, destination_to_town[i] + town_to_destination[i])

print(ans)

######################


### back_graph!!!!!!!!!라니
### 발상의 전환
## ex) 1 --> 2로 가는 거리를 2 --> 1로 간다고 생각하고
## input을 받아서 순서를 다르게 저장한다면
## 알고리즘을 단 2회만 순회하면 된다!!!!!!

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
back_graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    back_graph[v].append((u, w))

def dijkstra(start, graph):
    dist = [float("INF")] * (n+1)
    Q = [(0, start)]

    while Q:
        time, node = heapq.heappop(Q)
        if dist[node] > time:
            dist[node] = time
            for v, w in graph[node]:
                alt = time + w
                heapq.heappush(Q, (alt, v))

    return dist

result = dijkstra(x, graph)
back_result = dijkstra(x, back_graph)

result = max(result[i] + back_result[i] for i in range(1, n+1))
print(result)