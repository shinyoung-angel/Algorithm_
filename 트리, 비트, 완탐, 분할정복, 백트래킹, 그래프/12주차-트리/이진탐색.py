
def inorder(num):
    global value
    if num <= node:
        inorder(num*2)
        tree[num] = value
        value += 1
        inorder(num*2+1)


for tc in range(1, int(input())+1):
    node = int(input())

    tree = [0 for _ in range(node+1)]
    value = 1
    inorder(1)
    print('#{} {} {}'.format(tc, tree[1], tree[node//2]))