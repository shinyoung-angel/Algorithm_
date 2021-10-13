

for tc in range(1, int(input())+1):
    n, m, l = map(int, input().split())
    tree = [0 for _ in range(n+1)]

    for i in range(m):
        node, value = map(int, input().split())
        tree[node] = value


    for i in range(n, 0, -1):
        if i // 2 >= 1:
            tree[i//2] += tree[i]


    print('#{} {}'.format(tc, tree[l]))


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


