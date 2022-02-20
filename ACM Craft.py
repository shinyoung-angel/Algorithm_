from collections import deque


def check(start):
    queue = deque([start])
    visited = [0] * (n+1)
    visited[start] = 1
    depths = [0] * (n+1)
    depths[1] = time[start]
    depth = 1
    while queue:
        t = queue.popleft()

        depth += 1
        for idx, val in enumerate(tree):
            if t in val and not visited[idx]:
                queue.append(idx)
                visited[idx] = 1
                depths[depth] = max(depths[depth], time[idx])


    return depths


for tc in range(int(input())):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    tree = [[] for _ in range(n+1)]
    for _ in range(k):
        x, y = map(int, input().split())
        tree[x].append(y)
    destination = int(input())
    print(check(destination))


