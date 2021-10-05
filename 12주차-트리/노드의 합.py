

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

def postorder(num):

    if 2*num + 1 <= n:
        postorder(2*num)
        postorder(2*num+1)
        tree[num] = tree[2*num] + tree[2*num+1]

    elif num <= n//2:
        postorder(2*num)
        tree[num] = tree[2*num]

for tc in range(1, int(input())+1):
    n, m, l = map(int, input().split())
    tree = [0] * (n+1)

    for i in range(m):
        node, value = map(int, input().split())
        tree[node] = value

    postorder(1)
    print('#{} {}'.format(tc, tree[l]))

# --------------------


