from collections import deque


def check(start):
    order = 1
    queue = deque([(start, order)])
    # visited = [0] * (n+1)
    # visited[start] = 1
    depth_list = [0] * (n+1)
    depth_list[1] = time[start]

    while queue:
        node, depth = queue.popleft()


        for idx, val in enumerate(tree):
            if node in val:
                queue.append((idx, depth+1))
                # visited[idx] = 1
                depth_list[depth+1] = max(depth_list[depth+1], time[idx])


    return sum(depth_list)


for tc in range(int(input())):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    tree = [[] for _ in range(n+1)]
    for _ in range(k):
        x, y = map(int, input().split())
        tree[x].append(y)
    destination = int(input())
    print(check(destination))


