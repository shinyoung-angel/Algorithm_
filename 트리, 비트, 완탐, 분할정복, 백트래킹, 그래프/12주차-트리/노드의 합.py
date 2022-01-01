

for tc in range(1, int(input())+1):
    n, m, l = map(int, input().split())
    node = [0] * (n+1) + [0]

    for i in range(m):
        idx, value = map(int, input().split())
        node[idx] = value

    for i in range(n//2, 0, -1):
        node[i] += node[i*2] + node[i*2+1]

    print('#{} {}'.format(tc, node[l]))


### 후위 순회 활용

def postorder(st):
    if st <= n:
        postorder(2 * st)
        postorder(2 * st + 1)
        if 2 * st <= n:
            tree[st] += tree[2 * st]
        if 2 * st + 1 <= n:
            tree[st] += tree[2 * st + 1]


t = int(input())

for tc in range(1, t + 1):
    n, m, l = map(int, input().split())
    tree = [0] * (n + 1)
    for i in range(m):
        node, value = map(int, input().split())
        tree[node] = value

    postorder(1)
    print('#{} {}'.format(tc, tree[l]))


